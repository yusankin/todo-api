from fastapi.encoders import jsonable_encoder
import uvicorn
from fastapi import FastAPI, HTTPException
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


@app.delete("/todos/{index}")
async def delete_item(index: int):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="index is out of Range")

    todos.pop(index)
    return {"message": "delete is success"}


@app.patch("/todos/{index}")
async def update_item(index: int, item: models.Resistar_data):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="index is out of Range")
    current = todos[index]
    current_model = models.Resistar_data(**current.model_dump())
    update_data = item.model_dump(exclude_unset=True)
    update_item = current_model.copy(update=update_data)
    todos[index] = jsonable_encoder(update_item)
    return update_item


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
