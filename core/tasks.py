from celery import shared_task
from celery.task import periodic_task


@shared_task
def adding_task(x, y):
    return x + y
