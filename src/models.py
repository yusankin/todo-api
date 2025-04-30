from pydantic import BaseModel, Field
from datetime import datetime


class Resistar_data(BaseModel):
    title: str
    done: bool
    date: str = datetime.now().strftime("%Y年%m月%d日")
