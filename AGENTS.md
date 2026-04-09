# Hung-Yi Lee LLM Wiki Schema

This repository follows an LLM-wiki pattern for building a persistent, compounding knowledge base around Hung-Yi Lee's videos and related research.

## Layers

### 1. Raw Sources

Directory: `raw/`

- `raw/` is the source-of-truth layer.
- The LLM may read from raw sources, but should treat them as immutable.
- Raw data includes channel metadata and cached transcripts.
- New sources should be added to `raw/`, never rewritten in place unless the fetch itself is being refreshed.

### 2. Wiki

Directory: `wiki/`

- The wiki is LLM-maintained markdown.
- The LLM owns the structure, summaries, cross-references, and organization.
- Humans read the wiki; the LLM writes and updates it.
- `wiki/index.md` is content-oriented navigation.
- `wiki/log.md` is chronological and append-only.

### 3. Schema

Files: `AGENTS.md`, `SKILL.md`

- `AGENTS.md` defines the wiki maintenance conventions.
- `SKILL.md` defines how an answering agent should use the wiki at query time.
- Update these files when the workflow evolves.

## Operations

### Ingest

When new channel data or transcripts are added:

1. Update raw metadata or transcript caches.
2. Re-compile the wiki.
3. Append an entry to `wiki/log.md`.
4. Preserve old knowledge unless a newer source clearly supersedes it.

### Query

When answering a user question:

1. Read `wiki/index.md` first.
2. Read `wiki/topic-map.md`, `wiki/query-playbook.md`, and relevant topic/series pages.
3. Search cached transcripts before answering from memory.
4. Prefer transcript-grounded answers.
5. If the answer is a useful durable artifact, write a markdown brief into `outputs/query-briefs/` and `wiki/queries/`.

### Lint

Periodically health-check the wiki for:

- missing core files
- missing topic/series pages
- missing transcript coverage
- orphan query notes
- stale or contradictory summaries

### Graph

When building or updating the knowledge graph:

1. Run `python3 scripts/hungyi_kb.py graph build` after major transcript syncs.
2. The graph is persistent — `wiki/graph/graph.json` survives across sessions.
3. Every edge is tagged EXTRACTED, INFERRED, or AMBIGUOUS.
4. Community detection groups related concepts without embeddings (Louvain on graph topology).
5. `wiki/graph/GRAPH_REPORT.md` contains god nodes, surprising connections, and suggested questions.
6. Use `python3 scripts/hungyi_kb.py graph query "<question>"` for structure-based navigation.
7. Prefer graph-first navigation over keyword search when answering questions.

## Page Conventions

- Use markdown, not proprietary formats.
- Keep page names stable.
- Prefer short pages with strong links over monolithic notes.
- For generated pages, include compact stats when useful.
- Favor relative links inside the repo.

## Current Tooling

- `python3 scripts/hungyi_kb.py sync-metadata`
- `python3 scripts/hungyi_kb.py sync-transcripts`
- `python3 scripts/hungyi_kb.py compile`
- `python3 scripts/hungyi_kb.py search "<query>"`
- `python3 scripts/hungyi_kb.py build-brief "<query>"`
- `python3 scripts/hungyi_kb.py graph build`
- `python3 scripts/hungyi_kb.py graph query "<query>"`
- `python3 scripts/hungyi_kb.py graph report`
- `python3 scripts/hungyi_kb.py lint`

## Answering Standard

- Sound like Hung-Yi Lee's teaching method, not literal identity roleplay.
- Intuition first.
- Black-box framing before opening the mechanism.
- Highlight limitations and practical debugging takeaways.
- Be explicit when an answer is inferred across sources instead of directly supported by a transcript match.
