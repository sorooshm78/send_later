from fastapi import APIRouter
from schemas.messanger import Message


router = APIRouter()

# def task_func(min):
#     with open("log.txt", "a") as f:
#         f.write(f"task is done at time {min}\n")


@router.post("/eitaa/send/")
def send_message(message: Message):
    print(message)
    return {
        "detail":"done",
    }


@router.post("/eitaa/send-later/")
def send_message(message: Message):
    print(message)
    return {
        "detail":"done",
    }