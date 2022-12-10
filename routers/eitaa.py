from fastapi import APIRouter
from schemas.messanger import Message, SchedulerMessage
from core.config import scheduler


router = APIRouter()

@router.post("/send/")
def send_message(message: Message):
    return {
        "detail":"done",
    }

@router.post("/send-later/")
def send_message(message: SchedulerMessage):
    # scheduler.add_job(task_func, 'date', run_date=message.date_time, args=[message.date_time])    
    return {
        "detail":"done",
    }
