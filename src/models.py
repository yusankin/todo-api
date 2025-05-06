from typing import Union
from pydantic import BaseModel, Field
from datetime import datetime


class Resistar_data(BaseModel):
    title: Union[str, None] = None
    done: Union[bool, None] = None
    date: Union[str, None] = datetime.now().strftime("%Y年%m月%d日")
