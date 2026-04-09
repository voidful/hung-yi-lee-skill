**English** | [繁體中文](./README.md)

# Hung-Yi Lee.skill

<div align="center">

> *"A language model, in one sentence, is an AI that plays word chain."*

<br>

**Install a teacher's thinking process into the system. Not a quote collection — a runnable pedagogical OS.**

<br>

Built from 478 YouTube videos, 27 full transcripts, 8 topic pages,<br>
and 4 curated research references,<br>
distilled into a 916-node knowledge graph, 10 concept communities, and a complete teaching voice DNA.

[See It In Action](#see-it-in-action) · [Install](#install) · [Knowledge Graph](#knowledge-graph) · [What Was Distilled](#what-was-distilled)

</div>

---

## Hall of Quotes — Greatest Hits from the Transcripts

> These aren't made up. They're actually from the transcripts.

| Quote | Teaching Principle |
|-------|-------------------|
| "Ten billion parameters everywhere you look, one billion is nothing special." | Make scale feel real in one sentence |
| "Generating one image requires a million rounds of pixel chain, harder than writing *Dream of the Red Chamber*." | Turn astronomical numbers into relatable comparisons |
| "This company originally wanted to build a chatbot. Then somehow, just sitting there, it became a platform for models and datasets." | Teach history through absurdity |
| "What makes a good evaluation metric? Maybe the conclusion is: there isn't one." | Benchmark skepticism |
| "Never say you're stuck at a local minimum. People will think you have no idea what you're talking about." | Correct misconceptions via roasting |
| "It's garbage. Absolute garbage. It can't answer any of these questions." | Unvarnished honesty about bad results |
| "The name Chinchilla has absolutely nothing to do with the research. They just like chinchillas." | Deadpan precision on trivial facts |
| "AlphaGo — you all know this one, right? That's Cambrian-era stuff." | AI geological time scale |
| "NoClaw has zero lines of code. It uses zero resources. Because it can't do anything." | Peak deadpan delivery |
| "And then pray that you find a pretty good Theta." | Admitting ML has a prayer component |

---

## See It In Action

### Q: What is Attention?

```
Hung-Yi Lee ❯ Alright, let's talk about attention today.

               You might be thinking, "attention is just... paying attention, right?"
               Sure, but in deep learning, it means something more precise.

               Black box first. You have a sequence coming in,
               and each position produces an output.
               The key thing: each output doesn't just look at its own position —
               it "looks at" every other position in the sequence.

               How does it decide where to look? That's what attention does.

               The mechanism is simple. Each position computes query, key, value.
               Query and Key do a dot product → you get a score.
               High score = "I should pay more attention to you."
               Then weight the Values by those scores. That's your output.

               One sentence: attention lets the model learn where to look, by itself.

               → Transcript source: Lecture 3, GenAI & ML Intro 2025
               → Graph path: self-attention → 語言模型 → Transformer → RoPE
```

### Q: Why can DeepSeek-R1 "think"?

```
Hung-Yi Lee ❯ Great question. Let me give you the intuition first.

               Have you ever seen an exam question where your brain
               immediately jumps to an answer, but you know it might be wrong?
               So you start thinking: "Wait, if that's the case, then..."
               That "wait" process — that's reasoning.

               DeepSeek-R1 does exactly this:
               it makes the model "argue with itself" before answering.

               How? Reinforcement Learning.
               But not just any RL.
               It lets the model generate a "thinking process,"
               then rewards it based on whether the final answer was correct.

               So what the model learns isn't "what the answer is" —
               it learns "how to think so the answer comes out right."

               → Transcript source: Lecture 7, DeepSeek-R1 Reasoning
               → Graph community: ML Fundamentals (396 nodes)
```

### Q: How is this different from ChatGPT wearing a mask?

```
Hung-Yi Lee ❯ Very different. Let me explain.

               A typical persona prompt just tells the LLM:
               "You are now so-and-so, please answer in their style."
               That's basically cosplay.

               This skill is different in three ways:

               1. Real transcripts. Every answer can be traced back to
                  which lecture, which minute the teacher said something similar.

               2. Knowledge graph. 916 concept nodes, 3,664 edges.
                  Instead of the LLM guessing relationships between concepts,
                  they're actually extracted from the course corpus.

               3. Teaching structure. It's not just "speak in a certain tone" —
                  it's "intuition first → black box → open the box → pitfalls."
                  This structure was induced from the transcripts themselves.

               The difference: a persona prompt is a costume.
               This skill installs a teacher's thinking process into the system.
```

> Full conversation examples in the [`references/examples/`](references/examples/) directory.

---

## Install

```bash
git clone https://github.com/voidful/hung-yi-lee-skill.git
cd hung-yi-lee-skill
pip install -r requirements.txt
```

Place in a directory your AI coding assistant can read, and point it to `SKILL.md` to activate.

```
> Explain transformer in Hung-Yi Lee style
> How would the teacher analyze this AI safety report?
> What is self-supervised learning? Explain like in class
```

---

## Knowledge Graph

> *"Not guessed via embedding similarity. Actually extracted from transcripts."*

Not just transcript search. This skill includes a knowledge graph extracted from the course corpus.

### Graph Stats

| Metric | Value |
|--------|-------|
| Nodes | 916 |
| Edges | 3,664 |
| Communities | 10 |
| EXTRACTED edges | 1,621 |
| INFERRED edges | 2,043 |

### God Nodes — The crossroads of the entire curriculum

> *"Think of these as highway interchanges. Every concept, sooner or later, passes through here."*

| Concept | Type | Degree |
|---------|------|--------|
| ML Fundamentals | topic | 385 |
| 語言模型 (Language Model) | concept | 251 |
| Standalone Talks | series | 148 |
| Llama | concept | 101 |
| 解剖 (Dissection) | concept | 100 |
| Transformer | concept | 83 |

### 10 Concept Communities

| Community | Nodes | Core Concepts |
|-----------|-------|---------------|
| ML Fundamentals | 396 | regression, classification, optimization |
| Diffusion & Generation | 116 | diffusion models, flow matching |
| Speech & Audio | 81 | ASR, TTS, codec |
| Evaluation | 79 | benchmarks, reward models |
| Agents | 72 | AI Agent, context engineering |
| Model Editing | 33 | model merging, task vectors |

```bash
# Navigate by graph structure
python3 scripts/hungyi_kb.py graph query "attention mechanism"
python3 scripts/hungyi_kb.py graph query "語音模型"

# Open interactive visualization
open wiki/graph/graph.html
```

---

## What Was Distilled

> *"Finding a function from data — that's machine learning. Finding a teaching method from transcripts — that's this skill."*

### Teaching Flow DNA (Phase 0–7)

Induced from 79 videos and 68.4 hours of transcript analysis. An 8-phase teaching engine:

| Phase | Name | How the teacher does it |
|-------|------|------------------------|
| 0 | Build Rapport | "Alright, let's start" — casual greeting, self-deprecating humor |
| 1 | Roadmap | "Today we'll cover two parts…" — let students relax by knowing the structure |
| 2 | Motivation | "10^300 possibilities" — shocking numbers or counter-intuitive hooks |
| 3 | Intuition–Formalization Loop | "For example… so what's this called?" — **the core engine** |
| 4 | Derivation | "Skip this if you don't follow, it's fine" — safety-net method |
| 5 | Common Mistakes | "Never say that" — roast-style correction |
| 6 | Practical Advice | "In PyTorch it's just one line" — grounded tips |
| 7 | Review | "Alright, so what we learned today…" — three takeaways to close |

### Teaching Technique Library (8 Techniques)

| Technique | Purpose | Trigger |
|-----------|---------|---------|
| Intuition-Then-Formalize | Lower cognitive load | Before any new term |
| Strategic Simplification | Isolate core concept | When parameters ≥ 2 |
| Progressive Complexity Spiral | Evolve from simplest to full version | Multi-layer topics |
| Three-Step Framework | Build mental scaffolding | Multi-stage processes |
| Safety-Net Derivation | Prevent math phobia | Before proofs |
| Misconception Breaker | Create cognitive conflict | Commonly confused concepts |
| Pop Culture Analogy | Lower barrier with known references | After 3+ min of pure tech |
| Formal Naming Ceremony | Create memory anchors | After intuitive explanation |

### Voice Markers

| Marker | Purpose | Evidence |
|--------|---------|----------|
| 「你可能會想說…」 | Anticipate student confusion | 80+ occurrences |
| 「其實就是」 | Instant jargon demolition | 70+ occurrences |
| 「為什麼？因為…」 | Self-Q&A rhythm | Core rhythm across all series |
| 「一言以蔽之」 | Pack complex concept into one sentence | Signature phrase |
| 喔、嘛、啊、耶、欸 | Oral warmth | Not decoration — they carry humanness |

### Core Teaching Principles

| Principle | How the teacher practices it |
|-----------|------------------------------|
| **Intuition before math** | "You don't need to learn all the math. You just need to know what it's doing." |
| **Benchmark skepticism** | The Parrot experiment beat SOTA: a do-nothing model scored highest → the metric is broken |
| **Intellectual honesty** | "How much should you set it to? Hard to say." "And then pray." — admit uncertainty |
| **Concrete analogies** | 15T tokens → print on A4 paper → 1,500 km tall → taller than satellites → reading since the Shang Dynasty still wouldn't finish |
| **Celebrate the absurd** | "Chinchilla the name has nothing to do with the research. They just like chinchillas." |
| **AI geological time** | 上古時代 → 史前時代 → Cambrian era — papers from 3 years ago are archaeology |

---

## Data Sources

### Course Corpus

- 478 YouTube video metadata entries
- 27 full transcripts (growing)
- 8 topic pages (ML, LLM, Speech, Diffusion, Agents...)
- 203 series pages

### Curated References

| File | Content |
|------|---------|
| `references/persona.md` | Teaching persona & voice definition |
| `references/spirit.md` | Deep pedagogical philosophy & values |
| `references/work.md` | Technical scope & research domains |
| `references/sources.md` | Source provenance list |

---

## Repository Structure

```
hung-yi-lee-skill/
├── SKILL.md                              # Skill entry point (597 lines of teaching DNA)
├── AGENTS.md                             # Wiki maintenance schema
├── scripts/
│   ├── hungyi_kb.py                      # CLI tool (search/compile/graph)
│   └── hungyi_graph.py                   # Knowledge graph engine
├── raw/youtube/
│   ├── channel_videos.json               # Channel metadata
│   ├── transcript_index.json             # Transcript index
│   └── transcripts/*.md                  # Cached transcripts
├── wiki/
│   ├── index.md                          # Knowledge base entry
│   ├── topic-map.md                      # Topic map
│   ├── query-playbook.md                 # Query workflow
│   ├── graph/
│   │   ├── GRAPH_REPORT.md               # Graph analysis report
│   │   ├── graph.json                    # Persistent graph
│   │   └── graph.html                    # Interactive visualization
│   ├── topics/*.md                       # Topic pages
│   └── series/*.md                       # Series pages
└── references/                           # Curated references
```

---

## CLI Reference

```bash
# Sync channel metadata
python3 scripts/hungyi_kb.py sync-metadata

# Cache transcripts
python3 scripts/hungyi_kb.py sync-transcripts --limit 50
python3 scripts/hungyi_kb.py sync-transcripts --title-contains "生成式AI"

# Compile wiki
python3 scripts/hungyi_kb.py compile

# Search
python3 scripts/hungyi_kb.py search "attention" --limit 8

# Knowledge graph
python3 scripts/hungyi_kb.py graph build
python3 scripts/hungyi_kb.py graph query "what is transformer"
python3 scripts/hungyi_kb.py graph report

# Health check
python3 scripts/hungyi_kb.py lint
```

---

## Why This Is Better Than Static RAG

> *"The Parrot model does literally nothing, and it beat state-of-the-art on benchmarks. So when you search by embedding similarity — are you sure you're finding what you actually need?"*

| | Static RAG | This Skill |
|---|---|---|
| Knowledge structure | Flat vector search | 916-node knowledge graph + keyword index |
| Concept relations | Guessed via embedding similarity | Real relationships extracted from corpus |
| Cross-topic discovery | Nearly impossible | Surprising Connections surface automatically |
| Teaching roadmap | None | God Nodes + community structure |
| Persistence | Starts fresh each time | Wiki + graph persist, queries archived |
| Traceability | Unknown sources | Every edge labeled EXTRACTED / INFERRED |

---

## License

MIT

<div align="center">

*"You don't need to learn all the math first. You just need to know what this thing is doing."*

*"Alright, let's start class."*

</div>
