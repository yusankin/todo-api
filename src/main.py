import uvicorn
from fastapi import FastAPI
from src import models

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/todos/")
async def create_item(item: models.Resistar_data):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
