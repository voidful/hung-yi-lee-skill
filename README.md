[English](./README.en.md) | **繁體中文**

<div align="center">

> *「你不需要先學會所有的數學，你只需要先知道這個東西在幹嘛。」*

<br>

**李宏毅老師的教學作業系統。不是語錄合集，是可運行的教學框架。**

<br>

基於 478 支 YouTube 影片、27 份完整逐字稿、8 個主題頁面、<br>
4 份精選研究參考資料深度調研，<br>
建構 916 節點知識圖譜、10 個概念社群、完整的教學語感 DNA。

[看效果](#效果示例) · [安裝](#安裝) · [知識圖譜](#知識圖譜) · [蒸餾了什麼](#蒸餾了什麼)

</div>

---

### 問：什麼是 Attention？

```
李宏毅    ❯ 好，我們今天來講 attention。

            你可能會想說，attention 不就是「注意力」嗎？
            對，但在 deep learning 裡面，它的意思更精確。

            先講 black box。你有一個 sequence 進來，
            每個位置都產生一個 output。
            重點是：每個 output 不是只看自己那個位置，
            它會「看」整個 sequence 的其他位置。
            
            那它怎麼決定要看哪裡？這就是 attention 在做的事。

            機制很簡單。每個位置算出 query、key、value。
            Query 跟 Key 做 dot product，得到一個分數。
            分數高的，就代表「我應該多注意你」。
            然後用這些分數加權 Value，就是 output。

            一句話：attention 就是「讓模型自己學會該看哪裡」。
            
            → 逐字稿來源：【生成式人工智慧與機器學習導論2025】第3講
            → 圖譜路徑：self-attention → 語言模型 → Transformer → RoPE
```

### 問：為什麼 DeepSeek-R1 會「思考」？

```
李宏毅    ❯ 欸，這個問題很好。我們先講一個直覺。

            你有沒有遇過一種考試題，你看到題目，
            腦袋裡先冒出一個答案，但你知道那個答案可能是錯的？
            然後你會開始想：「等一下，如果是這樣的話…」
            這個「等一下」的過程，就是 reasoning。

            DeepSeek-R1 做的事情就是：
            讓模型在回答之前，先跟自己「吵一架」。

            怎麼做到？Reinforcement Learning。
            但不是隨便的 RL 喔。
            它讓模型自己產生一段「思考過程」，
            然後用結果的對錯來給 reward。

            所以模型學會的不是「答案是什麼」，
            而是「怎麼想才會對」。

            → 逐字稿來源：第七講 DeepSeek-R1 深度思考
            → 圖譜社群：ML Fundamentals (396 nodes)
```

### 問：這跟 ChatGPT 套個面具有什麼不同？

```
李宏毅    ❯ 很不一樣。讓我跟你講。

            一般的 persona prompt，就是告訴 LLM：
            「你現在是某某人，請用他的風格回答。」
            那其實就是 cosplay 嘛。

            這個 skill 不一樣的地方：
            
            1. 它有真正的逐字稿。每個回答都可以追溯到
               老師哪一堂課、哪一分鐘講過類似的東西。
            
            2. 它有知識圖譜。916 個概念節點、3664 條邊。
               不是靠 LLM 自己猜概念之間的關係，
               是從課程語料裡真的提取出來的。
            
            3. 它有教學結構。不只是「用某種語氣說話」，
               而是「先講直覺 → 再講 black box → 再打開盒子
               → 最後講陷阱」。這個架構是從逐字稿裡歸納的。

            所以差別是：persona prompt 是裝扮，
            這個 skill 是把一個老師的思考方式裝進系統裡。
```

> 完整對話記錄在 [`references/examples/`](references/examples/) 目錄。

---

## 安裝

```bash
git clone https://github.com/voidful/hung-yi-lee-skill.git
cd hung-yi-lee-skill
pip install -r requirements.txt
```

放到你的 AI coding assistant 可以讀取的目錄，讓它讀 `SKILL.md` 就能啟動。

```
> 用李宏毅老師的風格幫我解釋 transformer
> 老師會怎麼看這份 AI safety report？
> 什麼是 self-supervised learning？像老師上課那樣講
```

---

## 知識圖譜

不只是逐字稿搜尋。這個 skill 內建了從課程語料提取的知識圖譜。

### Graph Stats

| 指標 | 數值 |
|------|------|
| 節點 | 916 |
| 邊 | 3,664 |
| 社群 | 10 |
| EXTRACTED 邊 | 1,621 |
| INFERRED 邊 | 2,043 |

### God Nodes — 整個課程的交叉路口

| 概念 | 類型 | 連接度 |
|------|------|--------|
| ML Fundamentals | topic | 385 |
| 語言模型 | concept | 251 |
| Standalone Talks | series | 148 |
| Llama | concept | 101 |
| 解剖 | concept | 100 |
| Transformer | concept | 83 |

### 10 個概念社群

| 社群 | 節點數 | 核心概念 |
|------|--------|----------|
| ML Fundamentals | 396 | 機器學習基礎、regression、classification |
| Diffusion And Generation | 116 | 擴散模型、flow matching、生成 |
| Speech And Audio | 81 | 語音辨識、合成、codec |
| Evaluation | 79 | benchmark、reward model |
| Agents | 72 | AI Agent、context engineering |
| Model Editing | 33 | model merging、task vector |

```bash
# 用圖譜導航回答問題
python3 scripts/hungyi_kb.py graph query "attention mechanism"
python3 scripts/hungyi_kb.py graph query "語音模型"

# 打開互動式視覺化
open wiki/graph/graph.html
```

---

## 蒸餾了什麼

### 教學架構 DNA

每個回答都遵循從逐字稿歸納的教學結構：

1. **直覺先行** — 用一句話講核心概念
2. **Black Box** — 先講 input / output / objective
3. **開箱機制** — 打開盒子講裡面怎麼運作
4. **陷阱提醒** — 常見誤解、limitation、debug 觀點
5. **簡短回顧** — 一小段 recap 收尾

### 語感標記

| 標記 | 用途 |
|------|------|
| 「你可能會想說…」 | 預測學生疑問 |
| 「先講 black box」| 由外到內教學 |
| 「為什麼？因為…」 | 自問自答節奏 |
| 「這個跟老師講過的 X 有關…」 | 跨主題橋接 |
| 喔、嘛、啊、耶 | 口語感 |

### 核心教學精神

| 原則 | 說明 |
|------|------|
| **Benchmark 懷疑論** | 數字本身不是答案，要問「它量的是什麼？」|
| **知識誠實** | 區分事實與推論，不確定就直說 |
| **具體類比** | 把抽象概念變成日常生活的畫面 |
| **先講直覺再講數學** | 能被大學生聽懂才算講清楚 |

---

## 資料來源

### 課程語料

- 478 支 YouTube 影片 metadata
- 27 份完整逐字稿（持續擴充中）
- 8 個主題頁面（ML, LLM, Speech, Diffusion, Agents...）
- 203 個系列頁面

### 精選參考

| 文件 | 內容 |
|------|------|
| `references/persona.md` | 教學人設與語感定義 |
| `references/spirit.md` | 深層教學哲學與價值觀 |
| `references/work.md` | 技術範圍與研究領域 |
| `references/sources.md` | 資料來源清單 |

---

## 倉庫結構

```
hung-yi-lee-skill/
├── SKILL.md                              # Skill 進入點
├── AGENTS.md                             # Wiki 維護 schema
├── scripts/
│   ├── hungyi_kb.py                      # CLI 工具（搜尋/編譯/圖譜）
│   └── hungyi_graph.py                   # 知識圖譜引擎
├── raw/youtube/
│   ├── channel_videos.json               # 頻道 metadata
│   ├── transcript_index.json             # 逐字稿索引
│   └── transcripts/*.md                  # 快取的逐字稿
├── wiki/
│   ├── index.md                          # 知識庫入口
│   ├── topic-map.md                      # 主題地圖
│   ├── query-playbook.md                 # 查詢流程
│   ├── graph/
│   │   ├── GRAPH_REPORT.md               # 圖譜分析報告
│   │   ├── graph.json                    # 持久化圖譜
│   │   └── graph.html                    # 互動式視覺化
│   ├── topics/*.md                       # 主題頁面
│   └── series/*.md                       # 系列頁面
└── references/                           # 精選參考資料
```

---

## CLI 指令

```bash
# 同步頻道 metadata
python3 scripts/hungyi_kb.py sync-metadata

# 快取逐字稿
python3 scripts/hungyi_kb.py sync-transcripts --limit 50
python3 scripts/hungyi_kb.py sync-transcripts --title-contains "生成式AI"

# 編譯 wiki
python3 scripts/hungyi_kb.py compile

# 搜尋
python3 scripts/hungyi_kb.py search "attention" --limit 8

# 知識圖譜
python3 scripts/hungyi_kb.py graph build
python3 scripts/hungyi_kb.py graph query "什麼是 transformer"
python3 scripts/hungyi_kb.py graph report

# 健康檢查
python3 scripts/hungyi_kb.py lint
```

---

## 為什麼這比靜態 RAG 更好

| | 靜態 RAG | 這個 Skill |
|---|---|---|
| 知識結構 | 平面向量搜尋 | 916 節點知識圖譜 + keyword 索引 |
| 概念關聯 | 靠 embedding 相似度猜 | 從語料提取的真實關係 |
| 跨主題發現 | 幾乎不可能 | Surprising Connections 自動浮出 |
| 教學路線 | 無 | God Nodes + community 結構 |
| 累積性 | 每次重來 | Wiki + 圖譜持久化，查詢歸檔 |
| 可追溯 | 不確定來源 | 每條邊標記 EXTRACTED / INFERRED |

---

## License

MIT

<div align="center">

*「你不需要先學會所有的數學，你只需要先知道這個東西在幹嘛。」*

</div>
