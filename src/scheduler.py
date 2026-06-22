from apscheduler.schedulers.blocking import BlockingScheduler
from main import fetch_users

scheduler = BlockingScheduler()

@scheduler.scheduled_job(
  'cron',
  timezone="Asia/Kolkata",
  hour = 10,
  minute = 5,
)

def daily_job():
  fetch_users()

scheduler.start()
