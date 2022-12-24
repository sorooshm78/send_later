from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone


TIME_ZONE = "Asia/Tehran"

scheduler = BackgroundScheduler(timezone=timezone(TIME_ZONE))
scheduler.start()
