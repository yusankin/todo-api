# Python Lab: 📋 ToDo App
このプロジェクトは、FastAPI によるWeb APIと、StreamlitによるフロントエンドUIを組み合わせた、シンプルかつ拡張性のあるToDoアプリケーションです。
開発効率を重視しながら、CRUD操作、データ永続化、UI操作、起動テンプレートの整備までを一貫して行っています。

## 🎥 デモ動画

![demo](./TodoAppDemo.gif)

## ✅ 起動方法（FastAPI + Streamlit 同時起動） -> start.py を使って自動起動
```bash
python start.py
```

## 🎨 Streamlit UI機能一覧

|機能	|内容	|API連携|
|--|--|--|
|📋 ToDo一覧表示|現在のタスク一覧|GET /todos|
|➕ タスク追加|テキストと完了チェック付き|POST /todos/|
|🗑 タスク削除|各タスク横に削除ボタン|DELETE /todos/{id}|
|💾 保存|現在のToDoをJSONファイルに保存|POST /todos/save|
|📂 読み込み|ファイルからToDo一覧を復元|POST /todos/load|


---

## 🚀 使用技術

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic（v2系）
- Pytest
- Streamlit

---

## 📦 プロジェクト構成

## 📦 プロジェクト構成

```
todo-api/
├── src/  
│   ├── main.py            # FastAPIエントリーポイント  
│   └── file_io.py         # JSON保存・読み込み
├── todo_app.py             # Streamlitフロントエンド
├── start.py               # FastAPI + Streamlit 自動起動スクリプト
├── tests/
│   └── test_main.py       # pytestによるユニットテスト
├── data/
│   └── todolist.json      # 保存データ（自動生成）
├── README.md
└── requirements.txt
```

---

## ▶️ 実行方法

1. 仮想環境の作成（任意）

```bash
python -m venv .venv
source .venv/bin/activate  
```

2. パッケージインストール
```bash
pip install -r requirements.txt
```

3. サーバー起動
```bash
uvicorn src.main:app --reload
```

4. 自動ドキュメント確認：
```bash
http://127.0.0.1:8000/docs
```

## 📮 提供API一覧  
---

### ✅ ヘルスチェック
```bash
GET /health
レスポンス：{"status": "ok"}
```

---

### ✅ ToDo登録
```
POST /todos/
```
リクエストボディ（例）：
```json
{
  "title": "買い物に行く",
  "done": false
}
```
date はサーバー側で自動補完されます（例："2025年04月29日"）

レスポンス例
```json
{
  "title": "買い物に行く",
  "done": false,
  "date": "2025年04月29日"
}
```
---

### ✅ ToDo一覧取得
```bash
GET /todos
```
レスポンス例：
```json
[
  {
    "title": "買い物に行く",
    "done": false,
    "date": "2025年04月29日"
  },
  {
    "title": "掃除",
    "done": true,
    "date": "2025年04月29日"
  }
]
```

---

### ✅ ToDo削除
```bash
DELETE /todos/{index}
```
成功レスポンス
```json
{
  "message": "delete is success"
}
```
エラー時（例：存在しないindexを指定）  
```json
ステータスコード：404  
レスポンス：
{
  "detail": "index is out of Range"
}
```
備考  
index は0から始まるリストの順番で指定されます。
削除後、GET /todos で確認すると該当のToDoが消えていることを確認できます。

### ✅ ToDo更新（部分更新）
```bash
PATCH /todos/{index}
```

**更新可能なフィールド（いずれも任意）**
- title: str
- done: bool
- date: str（例："2025年05月07日"）

**リクエスト例（doneだけ変更）**
```json
{
  "done": true
}
```

レスポンス例
```json

{
  "title": "掃除",
  "done": true,
  "date": "2025年05月07日"
}
```

エラー例

存在しない index → 404 index is out of Range

### ✅ ToDo削除（UUID指定）
```bash
DELETE /todos/{id}
```
レスポンス例
```json
{
  "message": "delete is success"
}
```

### ✅ ToDo更新（UUID指定）
```bash
PATCH /todos/{id}
```
更新可能フィールド（いずれも任意）
```json
title: str
done: bool
date: str
```

リクエスト例
```json
{
  "done": true
}
```

レスポンス例
```json
{
  "id": "2a7e3a01-9d84-4d0d-a0c5-7d8cb5fdfd4a",
  "title": "掃除",
  "done": true,
  "date": "2025年05月08日"
}
```
### ✅ データ保存
```bash
POST /todos/save?filename=ファイル名（任意）
```
クエリ例:
```
POST /todos/save?filename=mytasks.json
```
レスポンス:
```json
{
  "message": "saved successfully",
  "filename": "mytasks.json"
}
```

### ✅ データ読み込み
```bash
POST /todos/load?filename=ファイル名（任意）
```
パス例:
```
POST /todos/load?filename=mytasks.json
```
レスポンス（読み込んだToDoリスト）:
```json
[
  {
    "id": "a1b2c3...",
    "title": "掃除",
    "done": true,
    "date": "2025年05月08日"
  },
  ...
]
```
## 🧾 データ構造（Pydanticモデル）
```python
from pydantic import BaseModel
from datetime import datetime

class Resistar_data(BaseModel):
    title: str
    done: bool
    date: str = datetime.now().strftime("%Y年%m月%d日")
```
※ date はリクエストボディで指定しなくても、サーバー側で自動設定されます。

🧪 テスト実行方法
```python
pytest
```