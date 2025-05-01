import uvicorn
from fastapi import FastAPI
from src import models

app = FastAPI()

todos: list[models.Resistar_data] = []


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/todos/")
async def create_item(item: models.Resistar_data):
    todos.append(item)
    return todos


@app.get("/todos")
async def get_item():
    return todos


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
