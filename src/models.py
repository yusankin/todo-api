from typing import Union
from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class TodoItem(BaseModel):
    # id: Union[str, None] = str(uuid.uuid4())
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: Union[str, None] = None
    done: Union[bool, None] = None
    # date: Union[str, None] = datetime.now().strftime("%Y年%m月%d日")
    date: Union[str, None] = Field(
        default_factory=lambda: datetime.now().strftime("%Y年%m月%d日")
    )
