from email.policy import default
from pydantic import BaseModel, Field
from datetime import datetime


class Info(BaseModel):
    title: str
    done: bool
    date: datetime = Field(default_factory=datetime.now())
