# Source Notes

This skill was first distilled on 2026-04-08 and then upgraded into a knowledge-base workflow on 2026-04-08.

## Structural Reference

- `titanwings/colleague-skill`
  - URL: <https://github.com/titanwings/colleague-skill>
  - Used for the idea of separating a skill into a work track and a persona track.

## YouTube Channel

- Channel:
  - <https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ>

## Sampled Subtitle Corpus

These videos were sampled directly through subtitle fetching on 2026-04-08:

- 2025-09-15
  - `【生成式人工智慧與機器學習導論2025】第１講：一堂課搞懂生成式人工智慧的原理`
  - <https://www.youtube.com/watch?v=TigfpYPJk1s>
- 2025-09-28
  - `【生成式人工智慧與機器學習導論2025】第3講：解剖大型語言模型`
  - <https://www.youtube.com/watch?v=8iFvM7WUUs8>
- 2025-12-22
  - `【生成式人工智慧與機器學習導論2025】第 10 講：語音語言模型發展史`
  - <https://www.youtube.com/watch?v=CbIPjrOj2Tc>
- 2026-03-15
  - `AI Agent (1/3)：核心技術 Context Engineering 基本概念解說`
  - <https://www.youtube.com/watch?v=urwDLyNa9FU>

Observed subtitle signals from this sample:

- frequent roadmap-setting near the start
- repeated use of `今天`, `接下來`, `所以`, `但是`, `為什麼`
- strong preference for intuition before internals
- regular discussion of limitations, benchmarks, and open problems

## Scholar Profile

- Hung-yi Lee Google Scholar:
  - <https://scholar.google.com/citations?user=DxLO11IAAAAJ&hl=en>
- Profile signals seen on 2026-04-08:
  - affiliation: National Taiwan University
  - interests: deep learning, spoken language understanding, speech processing

## Representative Papers Seen On The Scholar Profile

- `SUPERB: Speech Processing Universal Performance Benchmark` (2021)
- `Temporal Pattern Attention for Multivariate Time Series Forecasting` (2019)
- `Can Large Language Models Be an Alternative to Human Evaluations?` (2023)
- `Self-supervised Speech Representation Learning: A Review` (2022)
- `Mockingjay: Unsupervised Speech Representation Learning with Deep Bidirectional Transformer Encoders` (2020)
- `TERA: Self-Supervised Learning of Transformer Encoder Representation for Speech` (2021)
- `One-shot Voice Conversion by Separating Speaker and Content Representations with Instance Normalization` (2019)
- `LAMOL: Language Modeling for Lifelong Language Learning` (2019)
- `DistilHuBERT: Speech Representation Learning by Layer-wise Distillation of Hidden-unit BERT` (2022)
- `Audio Word2Vec: Unsupervised Learning of Audio Segment Representations Using Sequence-to-sequence Autoencoder` (2016)

## Notes On User-Provided Material

The user also supplied a draft emphasizing:

- the colleague-skill dual-track structure
- ML three-step framing
- black-box-first explanation
- a stronger roleplay-oriented persona

This skill keeps the useful structural pieces, but tones down unsupported caricature elements when the sampled subtitles did not strongly support them.

## Karpathy-Style KB Workflow

The user explicitly asked to move toward the knowledge-management pattern described by Andrej Karpathy:

- `raw/` contains source documents and transcript caches
- `wiki/` contains compiled markdown indexes and maps
- scripts incrementally maintain both sides
- query outputs can be written back as markdown dossiers

This repo now includes `scripts/hungyi_kb.py` to support that workflow.
