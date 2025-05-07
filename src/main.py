from fastapi.encoders import jsonable_encoder
import uvicorn
from fastapi import FastAPI, HTTPException
from src import models

app = FastAPI()

todos: list[models.TodoItem] = []


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/todos/")
async def create_item(item: models.TodoItem):
    todos.append(item)
    return todos


@app.get("/todos")
async def get_item():
    return todos


@app.delete("/todos/by-index/{index}")
async def delete_item_index(index: int):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="index is out of Range")

    todos.pop(index)
    return {"message": "delete is success"}


@app.delete("/todos/{id}")
async def delete_item_index(id: str):
    for num, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(num)
            return {"message": "delete is success"}

    raise HTTPException(status_code=404, detail="id cannot found")


@app.patch("/todos/by-index/{index}")
async def update_item_index(index: int, item: models.TodoItem):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="index is out of Range")
    current = todos[index]
    current_model = models.TodoItem(**current.model_dump())
    update_data = item.model_dump(exclude_unset=True)
    update_item = current_model.copy(update=update_data)
    todos[index] = update_item
    return jsonable_encoder(update_item)


@app.patch("/todos/{id}")
async def update_item_index(id: str, item: models.TodoItem):
    for num, todo in enumerate(todos):
        if todo.id == id:
            current_model = models.TodoItem(**todo.model_dump())
            update_data = item.model_dump(exclude_unset=True)
            update_item = current_model.copy(update=update_data)
            todos[num] = update_item
            return jsonable_encoder(update_item)

    raise HTTPException(status_code=404, detail="id cannot found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
