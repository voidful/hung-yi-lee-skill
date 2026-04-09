
# Hung-Yi Lee AI Knowledge Base

This wiki follows a Karpathy-style pattern:

- `raw/` stores source data such as channel metadata and cached transcripts.
- `wiki/` stores compiled markdown indexes and maps.
- `AGENTS.md` is the schema that tells the LLM how to maintain the wiki.
- `scripts/hungyi_kb.py` updates and queries the knowledge base.

## Current Snapshot

- Metadata sync time: `2026-04-08T08:43:38+00:00`
- Public video count: `478`
- Cached transcript files: `27`
- Cached transcript segments: `58457`

## Read This First

- [video-catalog.md](./video-catalog.md) - video and series catalog
- [topic-map.md](./topic-map.md) - concept clusters inferred from the corpus
- [teaching-style.md](./teaching-style.md) - distilled lecture patterns
- [coverage.md](./coverage.md) - transcript coverage and fetch status
- [query-playbook.md](./query-playbook.md) - how to answer against the wiki
- [log.md](./log.md) - chronological maintenance log

## Filed Query Notes

- [queries/什麼是-context-engineering.md](./queries/什麼是-context-engineering.md)
- [queries/什麼是-transformer-attention.md](./queries/什麼是-transformer-attention.md)


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

## Knowledge Graph (`916` nodes, `3664` edges)

- [GRAPH_REPORT.md](./graph/GRAPH_REPORT.md) — god nodes, surprising connections, suggested questions
- [graph.html](./graph/graph.html) — interactive visualization (open in browser)
- Graph JSON: `wiki/graph/graph.json` (query with `python3 scripts/hungyi_kb.py graph query "<question>"`)

## Notes

- Answers should prefer transcript-grounded evidence whenever possible.
- If a transcript is missing, the skill should fall back to topic pages, metadata, and the curated references.
- This wiki is intentionally markdown-first so an LLM can maintain it incrementally.
