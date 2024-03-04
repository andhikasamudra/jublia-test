from celery import Celery
from celery.schedules import crontab

app = Celery(
    "app",
    broker="redis://localhost:6379/0",
    include=["app.tasks"],
)

app.conf.beat_schedule = {
    "send-emails": {
        "task": "app.tasks.send_emails",
        "schedule": crontab(minute="*"),
    },
}

app.conf.timezone = "UTC"
