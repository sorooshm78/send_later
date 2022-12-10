from pydantic import BaseModel
from fastapi import Path


class Message(BaseModel):
    chat_id : int = Path(gt=0)
    text : str