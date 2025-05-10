import subprocess
import time
import requests

# FastAPI起動（バックグラウンド）
print("🚀 Starting FastAPI...")
fastapi_proc = subprocess.Popen(["uvicorn", "src.main:app", "--reload"])

# 少し待機してから Streamlit 起動
time.sleep(2)
todos_item_list = requests.get("http://localhost:8000/health")

print("🌈 Starting Streamlit...")
try:
    subprocess.run(["streamlit", "run", "todo_app.py"])
finally:
    # Streamlitを終了したらFastAPIも止める
    fastapi_proc.terminate()
    print("🛑 FastAPI server stopped.")
