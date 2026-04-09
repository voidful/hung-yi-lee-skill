
# Query Playbook

Use this workflow when answering a user as "Hung-Yi Lee style":

## Graph-First Navigation (Preferred)

Before searching raw transcripts, check the knowledge graph:

1. Read [wiki/graph/GRAPH_REPORT.md](./graph/GRAPH_REPORT.md) for god nodes and community structure.
2. Run:

```bash
python3 scripts/hungyi_kb.py graph query "<user question>"
```

3. The graph query returns relevant nodes, their community membership, and connecting paths.
4. Use the graph response to identify which transcripts to read — navigate by structure, not keyword.
5. Fall back to the keyword-based `search` command only if the graph query returns no relevant nodes.

## Keyword Search Fallback

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
