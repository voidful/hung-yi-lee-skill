[English](./README.en.md) | **繁體中文**

# Hung-Yi Lee Skill

一個 Karpathy 風格的 LLM wiki + skill，用於以李宏毅老師的教學風格回答 AI 相關問題。

這個 repo 不只是一個靜態的 persona prompt，而是一個持久化的 markdown 知識庫，會編譯：

- 原始頻道 metadata
- 快取的 YouTube 逐字稿
- 精選的教學風格參考資料
- 自動產生的 wiki 頁面，用於搜尋、綜合整理與問答

目標很簡單：

- 讓使用者提出 AI 相關問題
- 優先搜尋李宏毅老師的課程語料
- 以逐字稿作為答案的根據
- 以李宏毅老師的教學架構回答：先講直覺、再講機制、最後講陷阱

## 這個 Repo 包含什麼

- [SKILL.md](./SKILL.md)
  - agent 使用的 skill 進入點
- [AGENTS.md](./AGENTS.md)
  - 定義 wiki 維護方式的 schema
- [scripts/hungyi_kb.py](./scripts/hungyi_kb.py)
  - CLI 工具，支援抓取、編譯、搜尋、查詢摘要、健康檢查
- [raw/](./raw)
  - 不可變的原始資料，例如頻道 metadata 和快取的逐字稿
- [wiki/](./wiki)
  - 編譯後的 markdown 知識庫
- [references/](./references)
  - 精選的非逐字稿參考資料，關於風格、範圍和來源

## 架構

此 repo 遵循三層 LLM wiki 模式：

### 1. 原始資料層（Raw Sources）

- `raw/youtube/channel_videos.json`
- `raw/youtube/transcripts/*.md`
- `raw/youtube/transcript_index.json`

這些被視為 source-of-truth 輸入。Agent 可以讀取，但不應隨意修改。

### 2. Wiki 層

- `wiki/index.md`
- `wiki/topic-map.md`
- `wiki/coverage.md`
- `wiki/teaching-style.md`
- `wiki/query-playbook.md`
- `wiki/log.md`
- `wiki/topics/*.md`
- `wiki/series/*.md`
- `wiki/queries/*.md`

這是由 LLM 維護的層級，設計上會隨時間持續累積知識。

### 3. Schema 層

- `AGENTS.md`
- `SKILL.md`

這些檔案定義了 agent 作為維護者和查詢引擎的行為方式。

## 快速開始

### 1. 安裝逐字稿依賴套件

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. 同步頻道 metadata

```bash
python3 scripts/hungyi_kb.py sync-metadata
```

### 3. 快取部分逐字稿

先從一個可管理的批次開始：

```bash
python3 scripts/hungyi_kb.py sync-transcripts --limit 50
```

也可以針對特定系列：

```bash
python3 scripts/hungyi_kb.py sync-transcripts --title-contains "生成式人工智慧與機器學習導論2025"
```

### 4. 編譯 wiki

```bash
python3 scripts/hungyi_kb.py compile
```

### 5. 執行健康檢查

```bash
python3 scripts/hungyi_kb.py lint
```

### 6. 搜尋與產生查詢摘要

```bash
python3 scripts/hungyi_kb.py search "什麼是 transformer attention" --limit 6
python3 scripts/hungyi_kb.py build-brief "什麼是 transformer attention" --limit 6
```

這會寫入：

- 一份可重複使用的摘要到 `outputs/query-briefs/`
- 一份歸檔的 wiki 副本到 `wiki/queries/`
- 更新 `wiki/index.md` 以連結新的查詢筆記

## 建議的查詢流程

當使用者提問，例如：

> 老師，什麼是 transformer attention？

Agent 應該：

1. 讀取 [wiki/index.md](./wiki/index.md)。
2. 讀取 [wiki/topic-map.md](./wiki/topic-map.md) 以及最相關的主題頁面。
3. 執行：

```bash
python3 scripts/hungyi_kb.py search "什麼是 transformer attention" --limit 6
```

4. 如果有用，產生摘要：

```bash
python3 scripts/hungyi_kb.py build-brief "什麼是 transformer attention" --limit 6
```

5. 以下列結構回答：
   - 一句話的直覺
   - 黑箱觀點
   - 機制說明
   - 限制或常見誤解
   - 簡短回顧

## 目前狀態

截至目前的 repo 快照：

- 公開頻道的 metadata 已被索引
- 逐字稿快取已經開始
- Wiki 可以正常編譯
- Skill 已通過 `quick_validate.py` 驗證

隨著更多逐字稿被擷取，覆蓋率將持續提升。

## CLI 參考

### 同步 metadata

```bash
python3 scripts/hungyi_kb.py sync-metadata
```

從頻道擷取公開影片清單。

### 同步逐字稿

```bash
python3 scripts/hungyi_kb.py sync-transcripts --limit 80
python3 scripts/hungyi_kb.py sync-transcripts --title-contains "AI Agent"
python3 scripts/hungyi_kb.py sync-transcripts --force
```

將逐字稿快取為 markdown 檔案。

### 編譯 wiki

```bash
python3 scripts/hungyi_kb.py compile
```

從原始 metadata 和逐字稿快取建構 markdown wiki。

### 搜尋

```bash
python3 scripts/hungyi_kb.py search "model editing" --limit 8
```

搜尋標題和逐字稿段落。

### 產生摘要

```bash
python3 scripts/hungyi_kb.py build-brief "什麼是 post-training"
```

建立一份 markdown 摘要，包含：

- 候選來源
- 匹配的逐字稿行
- 段落上下文
- 建議的回答架構
- 並自動更新 wiki 索引

### 健康檢查

```bash
python3 scripts/hungyi_kb.py lint
```

檢查 wiki 的結構完整性。

## 逐字稿擷取注意事項

YouTube 可能回傳：

- `TranscriptsDisabled`
- `NoTranscriptFound`
- `IpBlocked`

這對某些影片來說是預期行為。此工作流程設計為漸進式：

- 先擷取目前可用的
- 編譯已有的
- 之後再重試
- 即使在部分覆蓋的情況下，wiki 仍然保持可用

## 為什麼這比靜態 RAG 更好

此 repo 在原始資料和回答之間維護了一個持久化的 markdown wiki。

這意味著：

- 綜合整理會持續累積
- 查詢摘要可以歸檔回 wiki
- 覆蓋率和缺口一目了然
- Agent 不需要每次從零開始重新探索

## 如果你想擴展它

建議的下一步：

- 在 `raw/` 下加入更多來源類型，例如論文、投影片和筆記
- 如果 markdown 語料變得龐大，之後加入更好的本地搜尋後端
- 加入更豐富的主題推論規則
- 加入矛盾和過期聲明的 lint 規則
- 逐步抓取更多早期的課程存檔
