**English** | [繁體中文](./README.md)

# Hung-Yi Lee Skill

A Karpathy-style LLM wiki + skill for answering AI questions in a Hung-Yi Lee-inspired teaching style.

This repo is not just a static persona prompt. It is a persistent markdown knowledge base that compiles:

- raw channel metadata
- cached YouTube transcripts
- curated teaching-style references
- generated wiki pages for search, synthesis, and Q&A

The goal is simple:

- let a user ask AI-related questions
- search Hung-Yi Lee's lecture corpus first
- ground the answer in transcript evidence
- respond with a Hung-Yi Lee-like teaching structure: intuition first, mechanism second, pitfalls third

## What This Repo Contains

- [SKILL.md](./SKILL.md)
  - the skill entrypoint used by the agent
- [AGENTS.md](./AGENTS.md)
  - the schema that defines how the wiki is maintained
- [scripts/hungyi_kb.py](./scripts/hungyi_kb.py)
  - the CLI for ingest, compile, search, query dossiers, and linting
- [raw/](./raw)
  - immutable source-like artifacts such as channel metadata and cached transcripts
- [wiki/](./wiki)
  - compiled markdown knowledge base
- [references/](./references)
  - curated non-transcript references about style, scope, and provenance

## Architecture

This repo follows the three-layer LLM wiki pattern:

### 1. Raw Sources

- `raw/youtube/channel_videos.json`
- `raw/youtube/transcripts/*.md`
- `raw/youtube/transcript_index.json`

These are treated as source-of-truth inputs. The agent reads them but should not freestyle over them.

### 2. Wiki

- `wiki/index.md`
- `wiki/topic-map.md`
- `wiki/coverage.md`
- `wiki/teaching-style.md`
- `wiki/query-playbook.md`
- `wiki/log.md`
- `wiki/topics/*.md`
- `wiki/series/*.md`
- `wiki/queries/*.md`

This is the LLM-maintained layer. It is designed to compound over time.

### 3. Schema

- `AGENTS.md`
- `SKILL.md`

These files define how the agent should behave as a disciplined maintainer and query engine.

## Quick Start

### 1. Install transcript dependency

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Sync channel metadata

```bash
python3 scripts/hungyi_kb.py sync-metadata
```

### 3. Cache some transcripts

Start with a manageable batch:

```bash
python3 scripts/hungyi_kb.py sync-transcripts --limit 50
```

You can also target a slice:

```bash
python3 scripts/hungyi_kb.py sync-transcripts --title-contains "生成式人工智慧與機器學習導論2025"
```

### 4. Compile the wiki

```bash
python3 scripts/hungyi_kb.py compile
```

### 5. Run a health check

```bash
python3 scripts/hungyi_kb.py lint
```

### 6. Search and build a query dossier

```bash
python3 scripts/hungyi_kb.py search "什麼是 transformer attention" --limit 6
python3 scripts/hungyi_kb.py build-brief "什麼是 transformer attention" --limit 6
```

This writes:

- a reusable brief in `outputs/query-briefs/`
- a filed wiki copy in `wiki/queries/`
- a refreshed `wiki/index.md` with the new query note linked

## Recommended Query Workflow

When a user asks something like:

> 老師，什麼是 transformer attention？

the agent should:

1. Read [wiki/index.md](./wiki/index.md).
2. Read [wiki/topic-map.md](./wiki/topic-map.md) and the most relevant topic page.
3. Run:

```bash
python3 scripts/hungyi_kb.py search "什麼是 transformer attention" --limit 6
```

4. If useful, generate a dossier:

```bash
python3 scripts/hungyi_kb.py build-brief "什麼是 transformer attention" --limit 6
```

5. Answer with:
   - one-sentence intuition
   - black-box framing
   - mechanism
   - limitations or misconceptions
   - short recap

## Current Status

As of the current repo snapshot:

- the public channel metadata has been indexed
- transcript caching has already started
- the wiki is compilable
- the skill is valid under `quick_validate.py`

Coverage will keep improving as more transcripts are fetched over time.

## CLI Reference

### Sync metadata

```bash
python3 scripts/hungyi_kb.py sync-metadata
```

Fetches the public video list from the channel.

### Sync transcripts

```bash
python3 scripts/hungyi_kb.py sync-transcripts --limit 80
python3 scripts/hungyi_kb.py sync-transcripts --title-contains "AI Agent"
python3 scripts/hungyi_kb.py sync-transcripts --force
```

Fetches transcript caches into markdown files.

### Compile wiki

```bash
python3 scripts/hungyi_kb.py compile
```

Builds the markdown wiki from raw metadata and transcript caches.

### Search

```bash
python3 scripts/hungyi_kb.py search "model editing" --limit 8
```

Searches titles and transcript passages.

### Build brief

```bash
python3 scripts/hungyi_kb.py build-brief "什麼是 post-training"
```

Creates a markdown dossier with:

- candidate sources
- matched transcript lines
- local passage context
- a suggested answer shape
- and automatically refreshes the wiki index

### Lint

```bash
python3 scripts/hungyi_kb.py lint
```

Checks the structural health of the wiki.

## Notes On Transcript Fetching

YouTube may return:

- `TranscriptsDisabled`
- `NoTranscriptFound`
- `IpBlocked`

This is expected for some videos. The workflow is designed to be incremental:

- fetch what is available now
- compile what you have
- retry later
- keep the wiki useful even under partial coverage

## Why This Is Better Than Static RAG

The repo keeps a persistent markdown wiki between raw sources and answers.

That means:

- syntheses accumulate
- query briefs can be filed back into the wiki
- coverage and gaps are visible
- the agent does less rediscovery from scratch on every question

## If You Want To Extend It

Good next steps:

- add more source types under `raw/` such as papers, slides, and notes
- add a better local search backend later if the markdown corpus grows large
- add richer topic inference rules
- add lint rules for contradictions and stale claims
- ingest more of the older course archives gradually
