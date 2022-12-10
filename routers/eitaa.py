from fastapi import APIRouter
from schemas.messanger import SendMessage


router = APIRouter()

# def task_func(min):
#     with open("log.txt", "a") as f:
#         f.write(f"task is done at time {min}\n")


@router.post("/eitaa/sendMessage/")
def send_message(message: SendMessage):
    print(message)
    return {
        "detail":"done",
    }