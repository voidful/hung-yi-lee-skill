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
## [2026-04-09 00:22:00] schema | fix stiff output for out-of-domain topics

- action: Updated `SKILL.md` and `wiki/query-playbook.md`
- reason: When using the skill to analyze a system card (Claude Mythos), the output lost the teaching voice entirely — no 「你可能會想說…」, no roadmap, no analogies, switching to blog-post/analyst style mid-answer
- root cause: When To Use was scoped too narrowly to ML teaching; no response shape existed for analytical/commentary tasks; query playbook had no fallback for out-of-KB topics
- fixes applied:
  - When To Use: added out-of-domain triggers (report analysis, explicit skill invocation)
  - Tone Persistence rule: once activated, teaching voice must persist to end of response
  - New response shape: Analyze A Report, System Card, Or News (6-step template)
  - Anti-Regression Guardrails: explicit list of patterns to avoid (menu branching, checklists, bolded taglines, analyst tone, Insight blocks)
  - Query Playbook Out-of-KB Fallback: maintain spirit principles even without transcript evidence
## [2026-04-09 00:45:00] schema | add flavor layer — voice rhythm, humor DNA, simplification instinct

- action: Updated `SKILL.md` and `references/spirit.md`
- reason: After structural fix, output still read like a competent analyst with Chinese transition phrases — missing the actual personality (short sentences, oral particles, genuine reactions, humor mechanisms, 「其實就是」demystification)
- key additions:
  - SKILL.md: Voice Rhythm And Flavor section with 5 subsections (Short Sentence Rhythm, Simplification Instinct, Genuine Reactions, Deadpan Absurd, 「其實就是」Demystification) — each with ❌/✅ before/after examples
  - SKILL.md: Report Analysis response shape rewritten to mandate flavor at every step with concrete examples
  - spirit.md: Humor Mechanisms with 5 named humor patterns from transcripts (casual bewilderment, exaggerated precision, mundane comparison, genuine surprise, blunt honesty)
  - spirit.md: Voice As Personality section — short sentence rhythm, self-answering questions, oral particles (喔嘛啊耶欸), 「其實就是」as jargon-buster
