#!/usr/bin/env python3
"""
Build and query a Karpathy-style markdown knowledge base for Hung-Yi Lee videos.

Workflow:
1. sync-metadata       -> fetch the full public channel video list
2. sync-transcripts    -> lazily or fully cache subtitles into markdown
3. compile             -> generate wiki pages from the raw cache
4. search              -> find relevant videos and transcript snippets
5. build-brief         -> write a markdown query dossier for later reading
6. lint                -> health-check the wiki structure
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "youtube"
WIKI_DIR = ROOT / "wiki"
OUTPUTS_DIR = ROOT / "outputs" / "query-briefs"
TRANSCRIPTS_DIR = RAW_DIR / "transcripts"
TOPICS_DIR = WIKI_DIR / "topics"
SERIES_DIR = WIKI_DIR / "series"
QUERY_NOTES_DIR = WIKI_DIR / "queries"
CHANNEL_INDEX_PATH = RAW_DIR / "channel_videos.json"
TRANSCRIPT_INDEX_PATH = RAW_DIR / "transcript_index.json"
LOG_PATH = WIKI_DIR / "log.md"

DEFAULT_CHANNEL_URL = "https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ/videos"
DEFAULT_LANGUAGES = ["zh-TW", "zh-Hant", "zh"]

TOPIC_RULES = {
    "ml-fundamentals": {
        "label": "ML Fundamentals",
        "keywords": [
            "機器學習",
            "deep learning",
            "類神經網路",
            "backpropagation",
            "regression",
            "classification",
            "訓練",
            "optimization",
        ],
    },
    "llm-and-transformers": {
        "label": "LLMs And Transformers",
        "keywords": [
            "語言模型",
            "大型語言模型",
            "transformer",
            "token",
            "kv cache",
            "flash attention",
            "positional",
            "rope",
            "attention",
            "reasoning",
        ],
    },
    "agents-and-context": {
        "label": "Agents And Context Engineering",
        "keywords": [
            "ai agent",
            "agent",
            "context engineering",
            "openclaw",
            "小龍蝦",
        ],
    },
    "speech-and-audio": {
        "label": "Speech And Audio",
        "keywords": [
            "語音",
            "speech",
            "audio",
            "voice",
            "spoken",
        ],
    },
    "diffusion-and-generation": {
        "label": "Diffusion And Generation",
        "keywords": [
            "diffusion",
            "flow",
            "生成",
            "autoregressive",
            "接龍",
        ],
    },
    "evaluation-and-benchmarks": {
        "label": "Evaluation And Benchmarks",
        "keywords": [
            "評估",
            "evaluation",
            "benchmark",
            "judge",
            "reward",
        ],
    },
    "model-editing-and-merging": {
        "label": "Model Editing / Merging / Lifelong Learning",
        "keywords": [
            "model editing",
            "editing",
            "model merging",
            "merging",
            "終身學習",
            "test-time training",
            "fine-tuning",
        ],
    },
    "interpretability": {
        "label": "Interpretability And Internal Mechanisms",
        "keywords": [
            "解剖",
            "內部",
            "腦科學",
            "神經元",
            "interpret",
        ],
    },
}

STYLE_MARKERS = [
    "今天",
    "課程目標",
    "我們先",
    "接下來",
    "所以",
    "但是",
    "為什麼",
    "真正",
    "注意",
    "總之",
]

STOP_QUERY_TOKENS = {
    "什麼",
    "什麼是",
    "請問",
    "老師",
    "如何",
    "為什麼",
    "怎麼",
    "可以",
    "the",
    "a",
    "an",
    "is",
    "are",
}


def ensure_dirs() -> None:
    for path in [
        RAW_DIR,
        WIKI_DIR,
        OUTPUTS_DIR,
        TRANSCRIPTS_DIR,
        TOPICS_DIR,
        SERIES_DIR,
        QUERY_NOTES_DIR,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def slugify(text: str) -> str:
    lowered = text.lower().strip()
    lowered = lowered.replace("&", " and ")
    lowered = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", lowered)
    lowered = re.sub(r"-{2,}", "-", lowered).strip("-")
    return lowered or "untitled"


def timestamp(seconds: float) -> str:
    total = int(seconds)
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text())


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def run_yt_dlp_json(url: str, flat: bool = False) -> dict:
    cmd = ["yt-dlp"]
    if flat:
        cmd.append("--flat-playlist")
    cmd.extend(["-J", url])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "yt-dlp failed")
    return json.loads(proc.stdout)


def parse_series(title: str) -> str:
    title = title.strip()
    if title.startswith("【") and "】" in title:
        return title[1 : title.index("】")].strip()
    if ":" in title:
        return title.split(":", 1)[0].strip()
    if "：" in title:
        return title.split("：", 1)[0].strip()
    if " - " in title:
        return title.split(" - ", 1)[0].strip()
    return "Standalone Talks"


def infer_topics(title: str) -> list[str]:
    lowered = title.lower()
    matched = []
    for slug, meta in TOPIC_RULES.items():
        if any(keyword.lower() in lowered for keyword in meta["keywords"]):
            matched.append(slug)
    if not matched:
        matched.append("ml-fundamentals")
    return matched


def metadata_entries() -> list[dict]:
    data = load_json(CHANNEL_INDEX_PATH, {})
    return data.get("videos", [])


def transcript_index() -> dict:
    return load_json(
        TRANSCRIPT_INDEX_PATH,
        {"generated_at": None, "videos": {}, "summary": {"fetched": 0, "missing": 0, "errors": 0}},
    )


def transcript_path(video_id: str) -> Path:
    return TRANSCRIPTS_DIR / f"{video_id}.md"


def parse_transcript_lines(path: Path) -> list[dict]:
    rows = []
    pattern = re.compile(r"^- \[(?P<stamp>\d{2}:\d{2}:\d{2})\] (?P<text>.*)$")
    for line in path.read_text().splitlines():
        match = pattern.match(line)
        if not match:
            continue
        rows.append({"timestamp": match.group("stamp"), "text": match.group("text")})
    return rows


def transcript_passages(path: Path, tokens: list[str], context_radius: int = 1, passage_limit: int = 2) -> list[dict]:
    rows = parse_transcript_lines(path)
    if not rows:
        return []

    matched_indices = []
    for idx, row in enumerate(rows):
        lowered = row["text"].lower()
        if any(token in lowered for token in tokens):
            matched_indices.append(idx)

    if not matched_indices:
        return []

    spans = []
    for idx in matched_indices:
        start = max(0, idx - context_radius)
        end = min(len(rows) - 1, idx + context_radius)
        if spans and start <= spans[-1][1] + 1:
            spans[-1][1] = max(spans[-1][1], end)
        else:
            spans.append([start, end])

    passages = []
    for start, end in spans[:passage_limit]:
        excerpt_lines = rows[start : end + 1]
        passages.append(
            {
                "start": excerpt_lines[0]["timestamp"],
                "end": excerpt_lines[-1]["timestamp"],
                "lines": [f"- [{row['timestamp']}] {row['text']}" for row in excerpt_lines],
            }
        )
    return passages


def sync_metadata(channel_url: str) -> None:
    ensure_dirs()
    payload = run_yt_dlp_json(channel_url, flat=True)
    entries = payload.get("entries", [])
    videos = []
    for index, entry in enumerate(entries, start=1):
        video_id = entry.get("id")
        title = entry.get("title", "").strip()
        if not video_id or not title:
            continue
        videos.append(
            {
                "playlist_position": index,
                "video_id": video_id,
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "series": parse_series(title),
                "topics": infer_topics(title),
            }
        )
    save_json(
        CHANNEL_INDEX_PATH,
        {
            "generated_at": now_iso(),
            "channel_title": payload.get("title"),
            "channel_url": channel_url,
            "video_count": len(videos),
            "videos": videos,
        },
    )
    append_log_entry(
        "ingest",
        "channel metadata sync",
        [
            f"channel_url: `{channel_url}`",
            f"video_count: `{len(videos)}`",
            f"output: `{CHANNEL_INDEX_PATH.relative_to(ROOT)}`",
        ],
    )
    print(f"Saved metadata for {len(videos)} videos -> {CHANNEL_INDEX_PATH}")


def fetch_transcript(video_id: str, languages: list[str]) -> tuple[list[dict] | None, str | None, str | None]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api._errors import (
            NoTranscriptFound,
            TranscriptsDisabled,
            VideoUnavailable,
        )
    except ImportError as exc:
        raise RuntimeError(
            "youtube-transcript-api is required. Install it with `python3 -m pip install youtube-transcript-api` "
            "or use a project virtual environment."
        ) from exc

    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(video_id, languages=languages)
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable) as exc:
        return None, None, type(exc).__name__
    except Exception as exc:  # noqa: BLE001
        return None, None, f"{type(exc).__name__}: {exc}"

    rows = [{"text": item.text.strip(), "start": item.start, "duration": item.duration} for item in fetched]
    language = getattr(fetched, "language_code", None)
    return rows, language, None


def write_transcript_markdown(video: dict, rows: list[dict], language: str | None) -> Path:
    path = transcript_path(video["video_id"])
    body_lines = [
        "---",
        f"video_id: {video['video_id']}",
        f"title: {json.dumps(video['title'], ensure_ascii=False)}",
        f"url: {video['url']}",
        f"series: {json.dumps(video['series'], ensure_ascii=False)}",
        f"topics: {json.dumps(video['topics'], ensure_ascii=False)}",
        f"transcript_language: {language or 'unknown'}",
        f"fetched_at: {now_iso()}",
        f"segment_count: {len(rows)}",
        "---",
        "",
        f"# {video['title']}",
        "",
        f"- Video: {video['url']}",
        f"- Series: `{video['series']}`",
        f"- Topics: {', '.join(video['topics'])}",
        "",
        "## Transcript",
        "",
    ]
    for row in rows:
        text = row["text"].replace("\n", " ").strip()
        if not text:
            continue
        body_lines.append(f"- [{timestamp(row['start'])}] {text}")
    path.write_text("\n".join(body_lines) + "\n")
    return path


def sync_transcripts(limit: int | None, title_contains: str | None, force: bool, languages: list[str]) -> None:
    ensure_dirs()
    videos = metadata_entries()
    if not videos:
        raise RuntimeError("Missing channel metadata. Run `sync-metadata` first.")

    query = title_contains.lower() if title_contains else None
    selected = []
    for video in videos:
        if query and query not in video["title"].lower():
            continue
        selected.append(video)
        if limit and len(selected) >= limit:
            break

    idx = transcript_index()
    fetched_now = 0
    missing_now = 0
    error_now = 0
    for video in selected:
        video_id = video["video_id"]
        path = transcript_path(video_id)
        if path.exists() and not force:
            existing = idx["videos"].get(video_id, {})
            existing.setdefault("status", "cached")
            idx["videos"][video_id] = existing
            continue

        rows, language, error = fetch_transcript(video_id, languages)
        if rows is None:
            idx["videos"][video_id] = {
                "title": video["title"],
                "url": video["url"],
                "status": "missing" if "NoTranscript" in (error or "") or "Disabled" in (error or "") else "error",
                "error": error,
                "updated_at": now_iso(),
            }
            print(f"[skip] {video_id} | {video['title']} | {error}")
            if idx["videos"][video_id]["status"] == "missing":
                missing_now += 1
            else:
                error_now += 1
            continue

        path = write_transcript_markdown(video, rows, language)
        idx["videos"][video_id] = {
            "title": video["title"],
            "url": video["url"],
            "status": "fetched",
            "language": language,
            "segment_count": len(rows),
            "path": str(path.relative_to(ROOT)),
            "updated_at": now_iso(),
        }
        print(f"[ok] {video_id} | {video['title']} | {language} | {len(rows)} segments")
        fetched_now += 1

    summary = Counter(item.get("status", "unknown") for item in idx["videos"].values())
    idx["generated_at"] = now_iso()
    idx["summary"] = {
        "fetched": summary.get("fetched", 0) + summary.get("cached", 0),
        "missing": summary.get("missing", 0),
        "errors": summary.get("error", 0),
    }
    save_json(TRANSCRIPT_INDEX_PATH, idx)
    append_log_entry(
        "ingest",
        "transcript sync",
        [
            f"selected_videos: `{len(selected)}`",
            f"fetched_now: `{fetched_now}`",
            f"missing_now: `{missing_now}`",
            f"errors_now: `{error_now}`",
            f"languages: `{', '.join(languages)}`",
        ],
    )
    print(f"Saved transcript index -> {TRANSCRIPT_INDEX_PATH}")


def transcript_stats() -> dict:
    idx = transcript_index()
    fetched_count = 0
    total_segments = 0
    total_lines = 0
    markers = Counter()
    for path in sorted(TRANSCRIPTS_DIR.glob("*.md")):
        text = path.read_text()
        total_lines += len(text.splitlines())
        for marker in STYLE_MARKERS:
            markers[marker] += text.count(marker)
        match = re.search(r"segment_count: (\d+)", text)
        if match:
            total_segments += int(match.group(1))
        fetched_count += 1
    return {
        "fetched_count": fetched_count,
        "total_segments": total_segments,
        "total_lines": total_lines,
        "markers": markers,
        "index_summary": idx.get("summary", {}),
        "status_breakdown": Counter(item.get("status", "unknown") for item in idx.get("videos", {}).values()),
    }


def write_markdown(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def append_log_entry(kind: str, title: str, details: list[str]) -> None:
    ensure_dirs()
    if not LOG_PATH.exists():
        write_markdown(LOG_PATH, "# Log\n")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"## [{stamp}] {kind} | {title}", ""]
    for detail in details:
        lines.append(f"- {detail}")
    lines.append("")
    with LOG_PATH.open("a") as handle:
        handle.write("\n".join(lines))


def compile_wiki() -> None:
    ensure_dirs()
    videos = metadata_entries()
    if not videos:
        raise RuntimeError("Missing channel metadata. Run `sync-metadata` first.")

    tstats = transcript_stats()
    by_series: dict[str, list[dict]] = defaultdict(list)
    by_topic: dict[str, list[dict]] = defaultdict(list)
    query_notes = sorted(QUERY_NOTES_DIR.glob("*.md"))
    for video in videos:
        by_series[video["series"]].append(video)
        for topic in video["topics"]:
            by_topic[topic].append(video)

    index_text = f"""
# Hung-Yi Lee AI Knowledge Base

This wiki follows a Karpathy-style pattern:

- `raw/` stores source data such as channel metadata and cached transcripts.
- `wiki/` stores compiled markdown indexes and maps.
- `AGENTS.md` is the schema that tells the LLM how to maintain the wiki.
- `scripts/hungyi_kb.py` updates and queries the knowledge base.

## Current Snapshot

- Metadata sync time: `{load_json(CHANNEL_INDEX_PATH, {}).get('generated_at', 'unknown')}`
- Public video count: `{len(videos)}`
- Cached transcript files: `{tstats['fetched_count']}`
- Cached transcript segments: `{tstats['total_segments']}`

## Read This First

- [video-catalog.md](./video-catalog.md) - video and series catalog
- [topic-map.md](./topic-map.md) - concept clusters inferred from the corpus
- [teaching-style.md](./teaching-style.md) - distilled lecture patterns
- [coverage.md](./coverage.md) - transcript coverage and fetch status
- [query-playbook.md](./query-playbook.md) - how to answer against the wiki
- [log.md](./log.md) - chronological maintenance log

## Filed Query Notes
"""
    if query_notes:
        latest_notes = "\n".join(
            f"- [queries/{path.name}](./queries/{path.name})" for path in query_notes[-10:]
        )
        index_text += f"\n{latest_notes}\n"
    else:
        index_text += "\n- No query notes filed yet.\n"

    index_text += f"""

## Quick Commands

```bash
python3 scripts/hungyi_kb.py sync-metadata
python3 scripts/hungyi_kb.py sync-transcripts --limit 50
python3 scripts/hungyi_kb.py compile
python3 scripts/hungyi_kb.py search "attention" --limit 8
python3 scripts/hungyi_kb.py build-brief "什麼是 attention"
python3 scripts/hungyi_kb.py graph build
python3 scripts/hungyi_kb.py graph query "attention mechanism"
python3 scripts/hungyi_kb.py lint
```
"""

    # Knowledge Graph section (only if graph outputs exist)
    graph_report = WIKI_DIR / "graph" / "GRAPH_REPORT.md"
    graph_json = WIKI_DIR / "graph" / "graph.json"
    if graph_report.exists() or graph_json.exists():
        graph_stats = ""
        if graph_json.exists():
            try:
                gdata = json.loads(graph_json.read_text(encoding="utf-8"))
                n_nodes = len(gdata.get("nodes", []))
                n_edges = len(gdata.get("links", []))
                graph_stats = f" (`{n_nodes}` nodes, `{n_edges}` edges)"
            except Exception:
                pass
        index_text += f"""
## Knowledge Graph{graph_stats}

- [GRAPH_REPORT.md](./graph/GRAPH_REPORT.md) — god nodes, surprising connections, suggested questions
- [graph.html](./graph/graph.html) — interactive visualization (open in browser)
- Graph JSON: `wiki/graph/graph.json` (query with `python3 scripts/hungyi_kb.py graph query "<question>"`)
"""

    index_text += """
## Notes

- Answers should prefer transcript-grounded evidence whenever possible.
- If a transcript is missing, the skill should fall back to topic pages, metadata, and the curated references.
- This wiki is intentionally markdown-first so an LLM can maintain it incrementally.
"""
    write_markdown(WIKI_DIR / "index.md", index_text)

    series_lines = ["# Video Catalog", "", f"Total indexed videos: `{len(videos)}`", ""]
    for series, items in sorted(by_series.items(), key=lambda pair: (-len(pair[1]), pair[0].lower())):
        series_slug = slugify(series)
        series_lines.append(f"## [{series}](./series/{series_slug}.md)")
        series_lines.append(f"Count: `{len(items)}`")
        series_lines.append("")
        for video in items[:25]:
            series_lines.append(f"- `{video['video_id']}` [{video['title']}]({video['url']})")
        if len(items) > 25:
            series_lines.append(f"- ... and {len(items) - 25} more")
        series_lines.append("")
    write_markdown(WIKI_DIR / "video-catalog.md", "\n".join(series_lines))

    topic_lines = ["# Topic Map", "", "Heuristic topic clusters inferred mostly from video titles.", ""]
    for topic, items in sorted(by_topic.items(), key=lambda pair: (-len(pair[1]), pair[0])):
        label = TOPIC_RULES.get(topic, {}).get("label", topic)
        topic_lines.append(f"## [{label}](./topics/{topic}.md)")
        topic_lines.append(f"Count: `{len(items)}`")
        topic_lines.append("")
        for video in items[:15]:
            topic_lines.append(f"- `{video['video_id']}` [{video['title']}]({video['url']})")
        if len(items) > 15:
            topic_lines.append(f"- ... and {len(items) - 15} more")
        topic_lines.append("")
    write_markdown(WIKI_DIR / "topic-map.md", "\n".join(topic_lines))

    status_breakdown = tstats["status_breakdown"]
    transcript_idx = transcript_index()
    pending_by_series = Counter()
    for video in videos:
        info = transcript_idx.get("videos", {}).get(video["video_id"], {})
        status = info.get("status")
        if status not in {"fetched", "cached"}:
            pending_by_series[video["series"]] += 1

    coverage_lines = [
        "# Coverage",
        "",
        "Transcript cache coverage across the indexed channel.",
        "",
        f"- Indexed videos: `{len(videos)}`",
        f"- Cached transcripts: `{tstats['fetched_count']}`",
        f"- Total transcript segments: `{tstats['total_segments']}`",
        "",
        "## Transcript Status Breakdown",
        "",
    ]
    for status, count in status_breakdown.most_common():
        coverage_lines.append(f"- `{status}`: {count}")
    coverage_lines.extend(["", "## Series With The Most Remaining Uncached Videos", ""])
    for series, count in pending_by_series.most_common(20):
        coverage_lines.append(f"- `{series}`: {count}")
    write_markdown(WIKI_DIR / "coverage.md", "\n".join(coverage_lines))

    style_lines = [
        "# Teaching Style",
        "",
        "This page is compiled from cached transcripts plus the curated references.",
        "",
        f"- Cached transcript files: `{tstats['fetched_count']}`",
        f"- Cached transcript segments: `{tstats['total_segments']}`",
        "",
        "## Recurrent Markers In Cached Transcripts",
        "",
    ]
    for marker, count in tstats["markers"].most_common():
        style_lines.append(f"- `{marker}`: {count}")
    style_lines.extend(
        [
            "",
            "## Stable Lecture Pattern",
            "",
            "1. Warm greeting.",
            "2. State today's topic and lesson goal.",
            "3. Give a roadmap such as `我們先... 接著... 最後...`.",
            "4. Explain the system as a black box first.",
            "5. Open the box and describe the mechanism.",
            "6. Point out caveats, limitations, or open problems.",
            "",
            "## Answering Preference",
            "",
            "- intuition before derivation",
            "- mechanism before jargon overload",
            "- concrete examples before abstraction drift",
            "- transcript-grounded teaching voice over generic textbook tone",
        ]
    )
    write_markdown(WIKI_DIR / "teaching-style.md", "\n".join(style_lines))

    query_playbook = """
# Query Playbook

Use this workflow when answering a user as "Hung-Yi Lee style":

1. Read [index.md](./index.md), [topic-map.md](./topic-map.md), and the most relevant topic page.
2. Run:

```bash
python3 scripts/hungyi_kb.py search "<user question>" --limit 8
```

3. Open the top matching transcript files in `raw/youtube/transcripts/`.
4. Distill the answer in a lecture structure:
   - one-sentence intuition
   - black-box framing
   - open-the-box mechanism
   - pitfalls or limitations
   - short recap
5. If transcript evidence is weak, say the answer is partly inferred from the broader course material.

## Optional Dossier Output

```bash
python3 scripts/hungyi_kb.py build-brief "<user question>"
```

This writes a markdown brief into `outputs/query-briefs/` so the LLM can re-open it later.
"""
    write_markdown(WIKI_DIR / "query-playbook.md", query_playbook)

    for topic, items in by_topic.items():
        label = TOPIC_RULES.get(topic, {}).get("label", topic)
        lines = [
            f"# {label}",
            "",
            f"Video count: `{len(items)}`",
            "",
            "Representative videos:",
            "",
        ]
        for video in items[:50]:
            transcript_rel = f"../../raw/youtube/transcripts/{video['video_id']}.md"
            transcript_suffix = f" | [transcript]({transcript_rel})" if transcript_path(video["video_id"]).exists() else ""
            lines.append(f"- [{video['title']}]({video['url']}){transcript_suffix}")
        write_markdown(TOPICS_DIR / f"{topic}.md", "\n".join(lines))

    for series, items in by_series.items():
        series_slug = slugify(series)
        lines = [
            f"# {series}",
            "",
            f"Video count: `{len(items)}`",
            "",
        ]
        for video in items:
            transcript_rel = f"../../raw/youtube/transcripts/{video['video_id']}.md"
            transcript_suffix = f" | [transcript]({transcript_rel})" if transcript_path(video["video_id"]).exists() else ""
            lines.append(f"- [{video['title']}]({video['url']}){transcript_suffix}")
        write_markdown(SERIES_DIR / f"{series_slug}.md", "\n".join(lines))

    if not LOG_PATH.exists():
        write_markdown(LOG_PATH, "# Log\n")
    append_log_entry(
        "compile",
        "wiki refresh",
        [
            f"video_count: `{len(videos)}`",
            f"topic_pages: `{len(by_topic)}`",
            f"series_pages: `{len(by_series)}`",
            f"cached_transcripts: `{tstats['fetched_count']}`",
        ],
    )
    print(f"Compiled wiki -> {WIKI_DIR}")


def tokenize_query(query: str) -> list[str]:
    raw = re.split(r"[\s,;:()\"'`/]+", query.lower())
    tokens = []
    for token in raw:
        token = token.strip()
        if not token or token in STOP_QUERY_TOKENS:
            continue
        tokens.append(token)
    return tokens


def transcript_snippets(path: Path, tokens: list[str], snippet_limit: int) -> list[str]:
    matches = []
    for line in path.read_text().splitlines():
        if not line.startswith("- ["):
            continue
        lowered = line.lower()
        if all(token not in lowered for token in tokens):
            continue
        matches.append(line)
        if len(matches) >= snippet_limit:
            break
    return matches


def search(query: str, limit: int) -> dict:
    videos = metadata_entries()
    tokens = tokenize_query(query)
    results = []
    for video in videos:
        title_lower = video["title"].lower()
        title_score = sum(3 for token in tokens if token in title_lower)
        transcript_file = transcript_path(video["video_id"])
        snippets = transcript_snippets(transcript_file, tokens, 3) if transcript_file.exists() else []
        passages = transcript_passages(transcript_file, tokens, context_radius=1, passage_limit=2) if transcript_file.exists() else []
        snippet_score = len(snippets) * 2
        passage_score = len(passages) * 3
        score = title_score + snippet_score + passage_score
        if score == 0:
            continue
        results.append(
            {
                "score": score,
                "video_id": video["video_id"],
                "title": video["title"],
                "url": video["url"],
                "series": video["series"],
                "topics": video["topics"],
                "transcript_path": str(transcript_file.relative_to(ROOT)) if transcript_file.exists() else None,
                "snippets": snippets,
                "passages": passages,
            }
        )
    results.sort(key=lambda item: (-item["score"], item["title"]))
    return {"query": query, "tokens": tokens, "results": results[:limit]}


def print_search_results(payload: dict) -> None:
    print(f"Query: {payload['query']}")
    print(f"Tokens: {', '.join(payload['tokens'])}")
    print("")
    for idx, item in enumerate(payload["results"], start=1):
        print(f"{idx}. score={item['score']} | {item['title']}")
        print(f"   video: {item['url']}")
        print(f"   series: {item['series']}")
        print(f"   topics: {', '.join(item['topics'])}")
        if item["transcript_path"]:
            print(f"   transcript: {item['transcript_path']}")
        for snippet in item["snippets"]:
            print(f"   snippet: {snippet}")
        for passage in item["passages"]:
            print(f"   passage: {passage['start']} -> {passage['end']}")
            for line in passage["lines"]:
                print(f"     {line}")
        print("")


def build_brief(query: str, limit: int) -> Path:
    ensure_dirs()
    payload = search(query, limit)
    slug = slugify(query)[:80]
    path = OUTPUTS_DIR / f"{slug}.md"
    lines = [
        f"# Query Brief: {query}",
        "",
        f"- Generated: `{now_iso()}`",
        f"- Query tokens: `{', '.join(payload['tokens'])}`",
        "",
        "## Suggested Answer Shape",
        "",
        "1. 用一句話先講核心直覺。",
        "2. 先把問題當成 black box，講 input / output / objective。",
        "3. 再打開盒子，講主要機制。",
        "4. 補常見誤解、限制或 debug 觀點。",
        "5. 最後用一小段 recap 收尾。",
        "",
        "## Candidate Sources",
        "",
    ]
    for item in payload["results"]:
        lines.append(f"### {item['title']}")
        lines.append(f"- Video: {item['url']}")
        lines.append(f"- Series: `{item['series']}`")
        lines.append(f"- Topics: `{', '.join(item['topics'])}`")
        if item["transcript_path"]:
            lines.append(f"- Transcript: `{item['transcript_path']}`")
        if item["snippets"]:
            lines.append("")
            lines.append("Matched transcript lines:")
            lines.append("")
            for snippet in item["snippets"]:
                lines.append(snippet)
        if item["passages"]:
            lines.append("")
            lines.append("Transcript passages:")
            lines.append("")
            for passage in item["passages"]:
                lines.append(f"Passage `{passage['start']}` -> `{passage['end']}`:")
                lines.append("")
                lines.extend(passage["lines"])
                lines.append("")
        lines.append("")
    write_markdown(path, "\n".join(lines))
    wiki_copy = QUERY_NOTES_DIR / path.name
    write_markdown(wiki_copy, "\n".join(lines))
    append_log_entry(
        "query",
        query,
        [
            f"results: `{len(payload['results'])}`",
            f"output: `{path.relative_to(ROOT)}`",
            f"wiki_copy: `{wiki_copy.relative_to(ROOT)}`",
        ],
    )
    compile_wiki()
    return path


def lint_wiki() -> None:
    ensure_dirs()
    videos = metadata_entries()
    tindex = transcript_index()
    problems = []

    if not CHANNEL_INDEX_PATH.exists():
        problems.append("missing raw/youtube/channel_videos.json")
    if not (WIKI_DIR / "index.md").exists():
        problems.append("missing wiki/index.md")
    if not LOG_PATH.exists():
        problems.append("missing wiki/log.md")

    series_count = len(list(SERIES_DIR.glob("*.md")))
    topic_count = len(list(TOPICS_DIR.glob("*.md")))
    if series_count == 0:
        problems.append("no compiled series pages")
    if topic_count == 0:
        problems.append("no compiled topic pages")

    fetched = tindex.get("summary", {}).get("fetched", 0)
    if fetched == 0:
        problems.append("no cached transcripts yet")

    missing_topic_assignments = [video["video_id"] for video in videos if not video.get("topics")]
    if missing_topic_assignments:
        problems.append(f"{len(missing_topic_assignments)} videos missing topic assignments")

    index_text = (WIKI_DIR / "index.md").read_text() if (WIKI_DIR / "index.md").exists() else ""
    orphan_queries = []
    for path in QUERY_NOTES_DIR.glob("*.md"):
        if path.name not in index_text:
            orphan_queries.append(path.name)
    if orphan_queries:
        problems.append(f"{len(orphan_queries)} query notes are not linked from wiki/index.md")

    summary_lines = [
        "# Lint Report",
        "",
        f"- Generated: `{now_iso()}`",
        f"- Problems found: `{len(problems)}`",
        "",
    ]
    if problems:
        summary_lines.append("## Findings")
        summary_lines.append("")
        for problem in problems:
            summary_lines.append(f"- {problem}")
    else:
        summary_lines.append("No structural issues found.")

    report_path = WIKI_DIR / "lint-report.md"
    write_markdown(report_path, "\n".join(summary_lines))
    append_log_entry(
        "lint",
        "wiki health check",
        [
            f"problems_found: `{len(problems)}`",
            f"report: `{report_path.relative_to(ROOT)}`",
        ],
    )
    print(report_path)
    if problems:
        for problem in problems:
            print(f"- {problem}")


GRAPH_DIR = WIKI_DIR / "graph"


def run_graph_build() -> None:
    """Build the full knowledge graph from transcripts, topics, and references."""
    from hungyi_graph import build_full_graph, query_graph, detect_communities

    ensure_dirs()
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    print("Building knowledge graph...")
    print(f"  Transcripts dir: {TRANSCRIPTS_DIR}")
    print(f"  Topics dir:      {TOPICS_DIR}")
    print(f"  References dir:  {ROOT / 'references'}")
    print()

    result = build_full_graph(
        transcripts_dir=TRANSCRIPTS_DIR,
        topics_dir=TOPICS_DIR,
        references_dir=ROOT / "references",
        channel_index_path=CHANNEL_INDEX_PATH,
        output_dir=GRAPH_DIR,
    )

    append_log_entry(
        "graph",
        "knowledge graph build",
        [
            f"nodes: `{result['graph_nodes']}`",
            f"edges: `{result['graph_edges']}`",
            f"communities: `{result['communities']}`",
            f"files_processed: `{result['stats']['files_processed']}`",
            f"output: `{GRAPH_DIR.relative_to(ROOT)}`",
        ],
    )

    # Re-compile wiki to include graph section
    compile_wiki()


def run_graph_query(query: str) -> None:
    """Query the knowledge graph by BFS traversal."""
    import networkx as nx
    from networkx.readwrite import json_graph as nx_json
    from hungyi_graph import detect_communities, query_graph

    graph_json = GRAPH_DIR / "graph.json"
    if not graph_json.exists():
        print("No graph found. Run `graph build` first.")
        return

    data = json.loads(graph_json.read_text(encoding="utf-8"))
    G = nx_json.node_link_graph(data, edges="links")
    partition = {n: d.get("community", 0) for n, d in G.nodes(data=True)}

    result = query_graph(G, partition, query)

    print(f"Query: {result['query']}")
    print(f"Tokens: {', '.join(result['tokens'])}")
    print()

    if not result["results"]:
        print("No matching nodes found.")
        return

    print(f"Found {len(result['results'])} relevant nodes:")
    print()
    for node in result["results"]:
        depth_marker = "  " * node["depth"]
        print(f"{depth_marker}• {node['label']} ({node['type']}) "
              f"[community {node['community']}, degree {node['degree']}]")

    if result["paths"]:
        print()
        print("Paths between seed nodes:")
        for p in result["paths"]:
            print(f"  {' → '.join(p['path'])} (length {p['length']})")


def run_graph_report() -> None:
    """Regenerate GRAPH_REPORT.md from existing graph.json."""
    import networkx as nx
    from networkx.readwrite import json_graph as nx_json
    from hungyi_graph import (
        detect_communities, label_communities, generate_report
    )

    graph_json = GRAPH_DIR / "graph.json"
    if not graph_json.exists():
        print("No graph found. Run `graph build` first.")
        return

    data = json.loads(graph_json.read_text(encoding="utf-8"))
    G = nx_json.node_link_graph(data, edges="links")
    partition = {n: d.get("community", 0) for n, d in G.nodes(data=True)}
    community_labels = label_communities(G, partition)

    stats = {
        "files_processed": G.number_of_nodes(),
        "transcripts": sum(1 for _, d in G.nodes(data=True) if d.get("type") == "video" and not d.get("metadata_only")),
        "metadata_only": sum(1 for _, d in G.nodes(data=True) if d.get("metadata_only")),
        "topic_pages": sum(1 for _, d in G.nodes(data=True) if d.get("type") == "topic"),
        "reference_docs": sum(1 for _, d in G.nodes(data=True) if d.get("type") == "reference"),
    }

    report = generate_report(G, partition, community_labels, stats)
    report_path = GRAPH_DIR / "GRAPH_REPORT.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report regenerated → {report_path}")


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    metadata = subparsers.add_parser("sync-metadata", help="Fetch the full public video list for the channel.")
    metadata.add_argument("--channel-url", default=DEFAULT_CHANNEL_URL)

    transcripts = subparsers.add_parser("sync-transcripts", help="Cache subtitles into raw/youtube/transcripts.")
    transcripts.add_argument("--limit", type=int, default=None)
    transcripts.add_argument("--title-contains", default=None)
    transcripts.add_argument("--force", action="store_true")
    transcripts.add_argument(
        "--languages",
        default=",".join(DEFAULT_LANGUAGES),
        help="Comma-separated preferred subtitle languages.",
    )

    subparsers.add_parser("compile", help="Compile wiki pages from raw metadata and cached transcripts.")
    subparsers.add_parser("lint", help="Run basic health checks over the wiki.")

    search_cmd = subparsers.add_parser("search", help="Search titles and cached transcripts.")
    search_cmd.add_argument("query")
    search_cmd.add_argument("--limit", type=int, default=8)

    brief_cmd = subparsers.add_parser("build-brief", help="Write a markdown dossier for a query.")
    brief_cmd.add_argument("query")
    brief_cmd.add_argument("--limit", type=int, default=8)

    # Graph subcommands
    graph_cmd = subparsers.add_parser("graph", help="Knowledge graph operations.")
    graph_sub = graph_cmd.add_subparsers(dest="graph_action", required=True)
    graph_sub.add_parser("build", help="Build the full knowledge graph.")
    graph_query = graph_sub.add_parser("query", help="Query the knowledge graph.")
    graph_query.add_argument("query")
    graph_sub.add_parser("report", help="Regenerate GRAPH_REPORT.md from existing graph.")

    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    if args.command == "sync-metadata":
        sync_metadata(args.channel_url)
        return 0
    if args.command == "sync-transcripts":
        languages = [item.strip() for item in args.languages.split(",") if item.strip()]
        sync_transcripts(args.limit, args.title_contains, args.force, languages)
        return 0
    if args.command == "compile":
        compile_wiki()
        return 0
    if args.command == "search":
        print_search_results(search(args.query, args.limit))
        return 0
    if args.command == "build-brief":
        path = build_brief(args.query, args.limit)
        print(path)
        return 0
    if args.command == "lint":
        lint_wiki()
        return 0
    if args.command == "graph":
        if args.graph_action == "build":
            run_graph_build()
            return 0
        if args.graph_action == "query":
            run_graph_query(args.query)
            return 0
        if args.graph_action == "report":
            run_graph_report()
            return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
