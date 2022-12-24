from fastapi import APIRouter
from schemas.messanger import Message, SchedulerMessage
from config.scheduler import scheduler
from messanger.bale import BaleMessanger


router = APIRouter()


@router.post("/send/")
def send_message(message: Message):
    messanger = BaleMessanger()
    result = messanger.send_message(text=message.text, receiver=message.chat_id)
    return result


@router.post("/send-later/")
def send_scheduler_message(message: SchedulerMessage):
    messanger = BaleMessanger()
    scheduler.add_job(
        messanger.send_message,
        "date",
        run_date=message.date_time,
        kwargs={
            "text": message.text,
            "receiver": message.chat_id,
        },
    )

    return {
        "detail": f"message will send at {message.date_time}",
    }
