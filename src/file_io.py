import json
from pathlib import Path
from typing import Union
from fastapi.encoders import jsonable_encoder
from src.models import TodoItem

PATH = Path("./data")


def save_data(todo_data, filename: str = "todolist.json") -> None:
    if filename[-5:] != ".json":
        filename = filename + ".json"
    data_file_path = PATH / filename
    with data_file_path.open("w", encoding="utf-8") as f:
        json.dump(jsonable_encoder(todo_data), f, ensure_ascii=False, indent=2)


def load_data(filename: Union[str, None] = "todolist.json"):
    if filename[-5:] != ".json":
        filename = filename + ".json"
    data_file_path = PATH / filename
    if data_file_path.exists():
        with data_file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []
