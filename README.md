# Python Lab: 📋 ToDo API

このプロジェクトは、FastAPIとPydanticを使って構築された**シンプルなToDo管理API**です。  
PythonとAPI設計・テストの基礎を理解することを目的にアジャイル的に開発しています。

---

## 🚀 使用技術

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic（v2系）
- Pytest

---

## 📦 プロジェクト構成

todo-api/  
 ├── src/   
 │ ├── main.py # APIエントリーポイント  
 │ └── models.py # Pydanticデータモデル   
 ├── tests/   
 │ └── test_todo.py # エンドポイントテスト   
 └── README.md


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
```bash
POST /todos/
リクエストボディ（例）：
{
  "title": "買い物に行く",
  "done": false
}
```
date はサーバー側で自動補完されます（例："2025年04月29日"）

レスポンス例
```bash
{
  "title": "買い物に行く",
  "done": false,
  "date": "2025年04月29日"
}
```
---

### ✅ ToDo一覧取得
```
GET /todos
レスポンス例：
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
DELETE /todos/{index}

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


🧾 データ構造（Pydanticモデル）
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
✅ テストの観点  
POSTでToDoを登録  
GETで一覧を取得し、登録内容と一致するか検証  
テスト間で todos を初期化するため fixture にて todos.clear() を実施  

💡 今後の発展案

PATCH /todos/{index} による状態更新  
DELETE /todos/{index} による削除機能  
SQLiteやファイルベースの永続化  
フロントエンドとの連携（React / HTML / REST Client）  