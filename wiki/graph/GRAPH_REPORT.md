# Knowledge Graph Report

Generated: `2026-04-09T13:23:12+00:00`

## Corpus

- Files processed: `490`
- Transcripts with graph coverage: `27`
- Metadata-only videos: `451`
- Topic pages: `8`
- Reference docs: `4`

## Graph Stats

- Nodes: `916`
- Edges: `3664`
- Communities: `10`
- EXTRACTED edges: `1621`
- INFERRED edges: `2043`
- AMBIGUOUS edges: `0`

## God Nodes

Highest-degree concepts — what everything connects through.

1. **Ml Fundamentals** (topic) — degree 385
2. **語言模型** (concept) — degree 251
3. **Standalone Talks** (series) — degree 148
4. **Llama** (concept) — degree 101
5. **解剖** (concept) — degree 100
6. **Diffusion And Generation** (topic) — degree 95
7. **Claude** (concept) — degree 88
8. **Gemini** (concept) — degree 86
9. **Transformer** (concept) — degree 83
10. **Language Model** (concept) — degree 74

## Communities

- **Ml Fundamentals** — 396 nodes
- **Diffusion And Generation** — 116 nodes
- **Speech And Audio** — 81 nodes
- **Review** — 80 nodes
- **Evaluation And Benchmarks** — 79 nodes
- **AI Agent (3/3)** — 72 nodes
- **Model Editing And Merging** — 33 nodes
- **Agents And Context** — 32 nodes
- **【生成式人工智慧與機器學習導論2025】第 5 講：一堂課搞懂機器學習與深度學習的基本原理 (案例：老師什麼時候要下課)** — 21 nodes
- **[ICASSP 2020] TRAINING CODE-SWITCHING LANGUAGE MODEL WITH MONOLINGUAL DATA (Speaker** — 6 nodes

## Surprising Connections

Edges that cross community boundaries — the non-obvious links.

1. **解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理** (video) ↔ **Claude** (concept) — mentions [EXTRACTED]
2. **Claude** (concept) ↔ **【生成式人工智慧與機器學習導論2025】第 2 講：上下文工程 (Context Engineering) — AI Agent 背後的關鍵技術** (video) — mentions [EXTRACTED]
3. **解剖** (concept) ↔ **【生成式AI時代下的機器學習(2025)】第七講：DeepSeek-R1 這類大型語言模型是如何進行「深度思考」（Reasoning）的？** (video) — mentions [EXTRACTED]
4. **解剖** (concept) ↔ **【生成式AI時代下的機器學習(2025)】第八講：大型語言模型的推理過程不用太長、夠用就好** (video) — mentions [EXTRACTED]
5. **語言模型** (concept) ↔ **【生成式人工智慧與機器學習導論2025】第 2 講：上下文工程 (Context Engineering) — AI Agent 背後的關鍵技術** (video) — mentions [EXTRACTED]
6. **語言模型** (concept) ↔ **AI Agent (1/3)：核心技術 Context Engineering 基本概念解說** (video) — mentions [EXTRACTED]
7. **【生成式人工智慧與機器學習導論2025】第3講：解剖大型語言模型** (video) ↔ **Llama** (concept) — mentions [EXTRACTED]
8. **【生成式人工智慧與機器學習導論2025】第3講：解剖大型語言模型** (video) ↔ **Gemma** (concept) — mentions [EXTRACTED]
9. **Deep Learning** (concept) ↔ **【生成式人工智慧與機器學習導論2025】第 10 講：語音語言模型發展史 (本課程前段內容為歷史回顧，2025 年的技術從 1:42:00 開始)** (video) — mentions [EXTRACTED]
10. **Llama** (concept) ↔ **【生成式AI時代下的機器學習(2025)】第十一講：今天你想為 Foundation Model 裝備哪些 Task Vector？淺談神奇的 Model Merging 技術** (video) — mentions [EXTRACTED]

## Suggested Questions

Questions the graph is uniquely positioned to answer:

- 「Ml Fundamentals」在李宏毅的課程中扮演什麼角色？為什麼這麼多概念都跟它有關？
- 「Ml Fundamentals」和「語言模型」之間是什麼關係？
- 為什麼「解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理」和「Claude」會有關聯？
- 為什麼「Claude」和「【生成式人工智慧與機器學習導論2025】第 2 講：上下文工程 (Context Engineering) — AI Agent 背後的關鍵技術」會有關聯？
- 「Agents And Context」和「AI Agent (3/3)」這兩個主題群之間有什麼交集？

## How To Use This Graph

```bash
python3 scripts/hungyi_kb.py graph query "attention mechanism"
python3 scripts/hungyi_kb.py graph query "語音模型"
python3 scripts/hungyi_kb.py graph report
```

Open `wiki/graph/graph.html` in any browser for interactive exploration.
