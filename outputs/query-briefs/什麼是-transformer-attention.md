# Query Brief: 什麼是 transformer attention

- Generated: `2026-04-08T08:57:26+00:00`
- Query tokens: `transformer, attention`

## Suggested Answer Shape

1. 用一句話先講核心直覺。
2. 先把問題當成 black box，講 input / output / objective。
3. 再打開盒子，講主要機制。
4. 補常見誤解、限制或 debug 觀點。
5. 最後用一小段 recap 收尾。

## Candidate Sources

### 【生成式AI時代下的機器學習(2025)】助教課：利用多張GPU訓練大型語言模型—從零開始介紹DeepSpeed、Liger Kernel、Flash Attention及Quantization
- Video: https://www.youtube.com/watch?v=mpuRca2UZtI
- Series: `生成式AI時代下的機器學習(2025)`
- Topics: `ml-fundamentals, llm-and-transformers, diffusion-and-generation`
- Transcript: `raw/youtube/transcripts/mpuRca2UZtI.md`

Matched transcript lines:

- [00:02:33] SashAttention
- [00:04:09] LagerKernel或是FlashAttention
- [00:12:29] 最佔空間的其實是Attention

Transcript passages:

Passage `00:02:32` -> `00:02:34`:

- [00:02:32] DeepSpeed
- [00:02:33] SashAttention
- [00:02:34] LagerKernel

Passage `00:04:08` -> `00:04:11`:

- [00:04:08] 你可能就會需要
- [00:04:09] LagerKernel或是FlashAttention
- [00:04:11] 這兩個工具


### 加快語言模型生成速度 (1/2)：Flash Attention
- Video: https://www.youtube.com/watch?v=vXb2QYOUzl4
- Series: `加快語言模型生成速度 (1/2)`
- Topics: `llm-and-transformers, diffusion-and-generation`
- Transcript: `raw/youtube/transcripts/vXb2QYOUzl4.md`

Matched transcript lines:

- [00:00:17] 你知道 Transformer 是怎麼運作的
- [00:00:21] 在你已經知道 Transformer 已經怎麼運作的前提之下
- [00:01:15] 就是 Transformer

Transcript passages:

Passage `00:00:14` -> `00:00:25`:

- [00:00:14] 語言模型內部的運作原理
- [00:00:17] 你知道 Transformer 是怎麼運作的
- [00:00:19] 那這一堂課是要跟你講說
- [00:00:21] 在你已經知道 Transformer 已經怎麼運作的前提之下
- [00:00:25] 我們怎麼加快生成的速度

Passage `00:01:12` -> `00:01:35`:

- [00:01:12] 今天主流的語言模型的類神經網路架構
- [00:01:15] 就是 Transformer
- [00:01:17] 那 Transformer 裡面有很多層
- [00:01:19] 有很多個 layer
- [00:01:20] 每個 layer 裡面呢
- [00:01:22] 都有一個機制叫做 self-attention
- [00:01:25] Self Attention
- [00:01:26] 讓 Transformer 可以考慮一整個輸入的 Sequence 裡面
- [00:01:30] 所有的資訊
- [00:01:32] 那這個 Self Attention 這個 Layer 呢
- [00:01:35] 它做的事情是這樣的


### 如何讓 Transformer 知道輸入 Token 的順序？Absolute、Relative、RoPE、到沒有 Positional Embedding
- Video: https://www.youtube.com/watch?v=Ll-wk8x3G_g
- Series: `Standalone Talks`
- Topics: `llm-and-transformers`
- Transcript: `raw/youtube/transcripts/Ll-wk8x3G_g.md`

Matched transcript lines:

- [00:00:04] 那這個技術它讓 Transformer 可以知道輸入 Token 的順序
- [00:00:10] 為什麼需要特別打造個技術讓 Transformer 知道輸入 Token 的順序呢
- [00:00:15] 因為原來的 Transformer 它是沒有辦法考慮輸入 Token 的順序的

Transcript passages:

Passage `00:00:00` -> `00:00:30`:

- [00:00:00] 好，今天我們這一堂課要講的是 Positional Embedding
- [00:00:04] 那這個技術它讓 Transformer 可以知道輸入 Token 的順序
- [00:00:10] 為什麼需要特別打造個技術讓 Transformer 知道輸入 Token 的順序呢
- [00:00:15] 因為原來的 Transformer 它是沒有辦法考慮輸入 Token 的順序的
- [00:00:23] 怎麼說呢，我們都知道大型語言模型
- [00:00:26] 它的背後就是一個叫
- [00:00:28] Transformer 的神經網路架構
- [00:00:30] 那它的輸入呢

Passage `00:00:33` -> `00:00:38`:

- [00:00:33] 就是去預測下一個 Token
- [00:00:36] 那 Transformer 怎麼處理
- [00:00:38] 這些輸入的 Token 呢


### 【生成式AI時代下的機器學習(2025)】第十二講：語言模型如何學會說話 — 概述語音語言模型發展歷程
- Video: https://www.youtube.com/watch?v=gkAyqoQkOSk
- Series: `生成式AI時代下的機器學習(2025)`
- Topics: `ml-fundamentals, llm-and-transformers, speech-and-audio, diffusion-and-generation`
- Transcript: `raw/youtube/transcripts/gkAyqoQkOSk.md`

Matched transcript lines:

- [00:37:50] 是用兩個transformer
- [00:37:52] 我們一般在做語音的時候只會有一個transformer
- [00:37:57] 可以有兩個transformer

Transcript passages:

Passage `00:37:48` -> `00:38:06`:

- [00:37:48] 那還有另外一個想法呢
- [00:37:50] 是用兩個transformer
- [00:37:52] 我們一般在做語音的時候只會有一個transformer
- [00:37:55] 但是在語音語言模型裡面
- [00:37:57] 可以有兩個transformer
- [00:37:59] 一個叫temporal transformer
- [00:38:00] 一個叫depth transformer
- [00:38:02] temporal transformer傳一個vector給
- [00:38:04] depth transformer
- [00:38:06] 再把第一個位置的每一個token

Passage `00:38:14` -> `00:38:25`:

- [00:38:14] 然後再生最細token的第一個
- [00:38:17] 然後呢 Temporal Transformer再給這個Depth Transformer下一個Vector
- [00:38:22] Depth Transformer呢,再生最粗的Token的第二個
- [00:38:25] 然後中間Token的第二個跟最細Token的第二個
