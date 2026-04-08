# Log
## [2026-04-08 16:43:38] ingest | channel metadata sync

- channel_url: `https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ/videos`
- video_count: `478`
- output: `raw/youtube/channel_videos.json`
## [2026-04-08 16:44:15] compile | wiki refresh

- video_count: `478`
- topic_pages: `8`
- series_pages: `203`
- cached_transcripts: `0`
## [2026-04-08 16:44:15] lint | wiki health check

- problems_found: `1`
- report: `wiki/lint-report.md`
## [2026-04-08 16:47:58] ingest | transcript sync

- selected_videos: `80`
- fetched_now: `27`
- missing_now: `22`
- errors_now: `31`
- languages: `zh-TW, zh-Hant, zh`
## [2026-04-08 16:48:15] compile | wiki refresh

- video_count: `478`
- topic_pages: `8`
- series_pages: `203`
- cached_transcripts: `27`
## [2026-04-08 16:48:15] query | 什麼是 transformer attention

- results: `6`
- output: `outputs/query-briefs/什麼是-transformer-attention.md`
- wiki_copy: `wiki/queries/什麼是-transformer-attention.md`
## [2026-04-08 16:48:15] lint | wiki health check

- problems_found: `1`
- report: `wiki/lint-report.md`
## [2026-04-08 16:48:24] compile | wiki refresh

- video_count: `478`
- topic_pages: `8`
- series_pages: `203`
- cached_transcripts: `27`
## [2026-04-08 16:48:24] lint | wiki health check

- problems_found: `0`
- report: `wiki/lint-report.md`
## [2026-04-08 16:49:09] compile | wiki refresh

- video_count: `478`
- topic_pages: `8`
- series_pages: `203`
- cached_transcripts: `27`
## [2026-04-08 16:49:09] lint | wiki health check

- problems_found: `0`
- report: `wiki/lint-report.md`
## [2026-04-08 16:57:26] query | 什麼是 transformer attention

- results: `4`
- output: `outputs/query-briefs/什麼是-transformer-attention.md`
- wiki_copy: `wiki/queries/什麼是-transformer-attention.md`
## [2026-04-08 16:57:26] compile | wiki refresh

- video_count: `478`
- topic_pages: `8`
- series_pages: `203`
- cached_transcripts: `27`
## [2026-04-08 16:57:26] lint | wiki health check

- problems_found: `0`
- report: `wiki/lint-report.md`
## [2026-04-08 16:58:30] query | 什麼是 context engineering

- results: `4`
- output: `outputs/query-briefs/什麼是-context-engineering.md`
- wiki_copy: `wiki/queries/什麼是-context-engineering.md`
## [2026-04-08 16:58:31] compile | wiki refresh

- video_count: `478`
- topic_pages: `8`
- series_pages: `203`
- cached_transcripts: `27`
## [2026-04-08 23:44:00] schema | SKILL.md and persona deep overhaul

- action: Rewrote `SKILL.md`, `references/persona.md`, and `wiki/teaching-style.md`
- reason: Deeper transcript analysis to capture Hung-Yi Lee's authentic teaching patterns
- key additions:
  - 10 named rhetorical moves with transcript-backed examples
  - 「你可能會想說」anticipation pattern
  - 「一言以蔽之」one-sentence-punch pattern
  - Scale-and-surprise with concrete numbers
  - Transition marker table with Chinese phrases
  - Vivid metaphor catalog (暗房裡的人, 擲骰子, 文字接龍, 餓狼下坡)
  - Expanded default response shape (10-step)
  - Paper explanation template
  - Debugging workflow with symptom-first approach
  - Enriched topic priorities with AI Agent and LLM architecture details
## [2026-04-08 23:52:00] schema | spirit deep-dive and SKILL.md philosophy integration

- action: Created `references/spirit.md`, updated `SKILL.md` with Teaching Spirit section and structured guardrails
- reason: Deeper transcript analysis focusing on philosophical values, not just rhetorical patterns
- transcripts analyzed in depth: TigfpYPJk1s (GenAI intro), Taj1eHmZyWw (ML fundamentals), dWQVY_h0YXU (evaluation pitfalls), YJoegm7kiUM (LLM learning journey), bJFtcwLSNxI (DeepSeek R1 reasoning), s266BzGNKKc (LLM evaluation issues), 2rcJdFuNbZQ (AI agents)
- key spirit principles added:
  - Intellectual Honesty First — say when things are hard, uncertain, or heuristic
  - Scale Demystification — make numbers tangible (15T tokens = 1500km of A4 paper)
  - Benchmark Skepticism — Goodhart's Law, Parrot experiment, leaderboard contamination
  - Progressive Formalism — name → intuition → formula → code, never formula-first
  - Analogy Lifecycle — introduce, stretch, break, formalize
  - Research as Living Process — papers-as-data-points, geological time scale (上古時代, 寒武紀)
  - Celebrating The Absurd — HuggingFace origin, Microwave GAN, NoClaw
  - Structured guardrails: Honesty, Metric, Style, Analogy categories
