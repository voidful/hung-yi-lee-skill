# Query Brief: 什麼是 context engineering

- Generated: `2026-04-08T08:58:30+00:00`
- Query tokens: `context, engineering`

## Suggested Answer Shape

1. 用一句話先講核心直覺。
2. 先把問題當成 black box，講 input / output / objective。
3. 再打開盒子，講主要機制。
4. 補常見誤解、限制或 debug 觀點。
5. 最後用一小段 recap 收尾。

## Candidate Sources

### AI Agent (1/3)：核心技術 Context Engineering 基本概念解說
- Video: https://www.youtube.com/watch?v=urwDLyNa9FU
- Series: `AI Agent (1/3)`
- Topics: `agents-and-context`
- Transcript: `raw/youtube/transcripts/urwDLyNa9FU.md`

Matched transcript lines:

- [00:00:16] 我們比較系統化地來講 Context Engineering
- [00:00:34] Context Engineering 開始講起
- [00:00:41] Context Engineering 的技術

Transcript passages:

Passage `00:00:13` -> `00:00:20`:

- [00:00:13] 我們來講 AI Agent 背後的核心技術
- [00:00:16] 我們比較系統化地來講 Context Engineering
- [00:00:20] 然後第二段呢

Passage `00:00:30` -> `00:00:36`:

- [00:00:30] 那我們就先從 AI Agent 的核心技術
- [00:00:34] Context Engineering 開始講起
- [00:00:36] 那等一下這段課程啊


### 【生成式人工智慧與機器學習導論2025】第 2 講：上下文工程 (Context Engineering) — AI Agent 背後的關鍵技術
- Video: https://www.youtube.com/watch?v=lVdajtNpaGI
- Series: `生成式人工智慧與機器學習導論2025`
- Topics: `ml-fundamentals, agents-and-context, diffusion-and-generation`
- Transcript: `raw/youtube/transcripts/lVdajtNpaGI.md`

Matched transcript lines:

- [00:00:03] 我們要講什麼是 Context Engineering
- [00:00:10] 那我們今天會介紹 Context Engineering 的概念
- [00:00:14] 告訴你說它跟你熟悉的 Prompt Engineering

Transcript passages:

Passage `00:00:00` -> `00:00:23`:

- [00:00:00] 好，今天這個第二堂課呢
- [00:00:03] 我們要講什麼是 Context Engineering
- [00:00:07] 這是一個最近很熱門的 Buzzword
- [00:00:10] 那我們今天會介紹 Context Engineering 的概念
- [00:00:14] 告訴你說它跟你熟悉的 Prompt Engineering
- [00:00:18] 有什麼差異
- [00:00:20] 那這個 Context Engineering
- [00:00:23] 是今天在 AI Agent 的時代

Passage `00:00:59` -> `00:01:07`:

- [00:00:59] 那兩堂課都聽完你會有不一樣的收穫
- [00:01:04] 好，那什麼是 Context Engineering 呢？
- [00:01:07] 我們不斷反覆強調說


### 【生成式AI時代下的機器學習(2025)】助教課：利用多張GPU訓練大型語言模型—從零開始介紹DeepSpeed、Liger Kernel、Flash Attention及Quantization
- Video: https://www.youtube.com/watch?v=mpuRca2UZtI
- Series: `生成式AI時代下的機器學習(2025)`
- Topics: `ml-fundamentals, llm-and-transformers, diffusion-and-generation`
- Transcript: `raw/youtube/transcripts/mpuRca2UZtI.md`

Matched transcript lines:

- [00:04:00] 那它可能的Context就會到
- [00:04:03] 128K這麼長的Context
- [00:15:26] 它在訓練32K的context的時候

Transcript passages:

Passage `00:03:57` -> `00:04:06`:

- [00:03:57] 如果你用的是Reasoning的Model
- [00:04:00] 那它可能的Context就會到
- [00:04:01] 32K或甚至
- [00:04:03] 128K這麼長的Context
- [00:04:06] 那在這個情況下

Passage `00:15:25` -> `00:15:29`:

- [00:15:25] 的某一個階段
- [00:15:26] 它在訓練32K的context的時候
- [00:15:29] 它的batch size是


### 【生成式AI時代下的機器學習(2025)】第六講：生成式人工智慧的後訓練(Post-Training)與遺忘問題
- Video: https://www.youtube.com/watch?v=Z6b5-77EfGk
- Series: `生成式AI時代下的機器學習(2025)`
- Topics: `ml-fundamentals, diffusion-and-generation`
- Transcript: `raw/youtube/transcripts/Z6b5-77EfGk.md`

Matched transcript lines:

- [00:35:15] 是孫凡根同學,那時候他是大學生,還有研究助理何正豪同學做的,那時候構想就是這一些自然語言處理的任務,他們都有一樣的格式,就是會先給模型看一段文字,那段文字當時叫做context,接下來你問他一個問題,他得輸出一個答案,也許有辦法直接用語言模型來做這件事情,就讓語言模型直接讀context,讀問題,然後接下來
- [00:46:52] 我們教他看到這個context
- [00:47:04] context問題跟答案

Transcript passages:

Passage `00:35:14` -> `00:35:45`:

- [00:35:14] 這個是
- [00:35:15] 是孫凡根同學,那時候他是大學生,還有研究助理何正豪同學做的,那時候構想就是這一些自然語言處理的任務,他們都有一樣的格式,就是會先給模型看一段文字,那段文字當時叫做context,接下來你問他一個問題,他得輸出一個答案,也許有辦法直接用語言模型來做這件事情,就讓語言模型直接讀context,讀問題,然後接下來
- [00:35:45] 來給一個代表answer的token,他就開始把答案接出來,直到他接到end of sentence為止,他輸出答案就停止了,好,不過因為當時啊,就算有GPT-2,那個GPT-2呢,就是廢的跟垃圾一樣,他是沒辦法直接回答這些問題的,所以需要做一些post training,需要微調GPT-2才有辦法做剛才的投影片裡面看到的任務,比如說假設你想要叫GPT-2做閱讀測驗,那你得先在一個

Passage `00:46:49` -> `00:46:55`:

- [00:46:49] 我們在教模型任務一的時候
- [00:46:52] 我們教他看到這個context
- [00:46:55] 看到這個問題
