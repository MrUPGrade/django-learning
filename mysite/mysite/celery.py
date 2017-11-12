import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.task_routes = {
    'basics.tasks.queue_test': {'queue': 'slow'},
    '*': {'queue': 'celery'},
}