import time

from celery import Celery
from celery.schedules import crontab

from app.middleware.Lottery import close_lottery
from app.settings import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


celery.conf.update(
    timezone='UTC',
    enable_utc=True,
    beat_schedule={
        # 'run-every-30-seconds': {
        #     'task': 'celery_worker.periodic_task',
        #     'schedule': 3.0,  # Run every 30 seconds
        # },
        'close-lottery-at-midnight': {
            'task': 'celery_worker.lottery_task',
            'schedule': crontab(minute=0, hour=0),
        },
    }
)

@celery.task
def periodic_task():
    print("Periodic pilot task is running")

@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    print(b + c)

@celery.task
def lottery_task():
    close_lottery()



@celery.task(name="win_partecipant")
def win_partecipant_task():
    time.sleep(5)
    # notify the partecipant
