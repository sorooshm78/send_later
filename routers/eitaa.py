from fastapi import APIRouter
from schemas.messanger import Message, SchedulerMessage
from core.config import scheduler
from messanger.eitaa import EitaaMessanger


router = APIRouter()

@router.post("/send/")
def send_message(message: Message):
    messanger = EitaaMessanger()
    result = messanger.send_message(text=message.text, receiver=message.chat_id)
    return result

@router.post("/send-later/")
def send_scheduler_message(message: SchedulerMessage):
    messanger = EitaaMessanger()
    scheduler.add_job(
        messanger.send_message,
        'date', run_date=message.date_time, 
        kwargs={
            'text':message.text, 
            'receiver':message.chat_id,
        }
    )    

    return {
        "detail":f"message will send at {message.date_time}",
    }
