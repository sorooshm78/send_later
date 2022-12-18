from pydantic import BaseModel, validator
from fastapi import Path
from datetime import datetime


now = datetime.now()


class Message(BaseModel):
    chat_id: int = Path(ge=0)
    text: str


class SchedulerMessage(Message):
    date_time: datetime = datetime.now().strftime("%Y-%m-%d %H:%M")

    @validator("date_time")
    def checking_datetime_not_before_now(cls, datetime_value):
        if datetime_value <= datetime.now():
            raise ValueError("datetime is not before now")

        return datetime_value
