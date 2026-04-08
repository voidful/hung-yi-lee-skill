
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
