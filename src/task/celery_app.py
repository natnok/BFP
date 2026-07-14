from celery import Celery

from src.config import settings

celery_instance = Celery(
    "tasks",
    broker=settings.REDIS_URL,
    include=["src.task.tasks"],
)


celery_instance.conf.beat_schedule = {
    "task": {
        "task": "beat_task",
        "schedule": 5,
    }
}
