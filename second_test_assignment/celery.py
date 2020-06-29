import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_test_assignment.settings')
celery_app = Celery('second_test_assignment')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
