from src.task.celery_app import celery_instance


@celery_instance.task(name="task_1")
def task_1():
    print("i'm normal task!")


@celery_instance.task(name="beat_task")
def task_2():
    print("i'm beat task!")
