from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from pytz import timezone

from routers import eitaa


TIME_ZONE = "Asia/Tehran"


scheduler = BackgroundScheduler(timezone=timezone(TIME_ZONE))
scheduler.start()

app = FastAPI()
app.include_router(eitaa.router, tags=["eitaa"])
