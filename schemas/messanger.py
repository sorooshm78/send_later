from pydantic import BaseModel


class SendMessage(BaseModel):
    chat_id : int
    text : str