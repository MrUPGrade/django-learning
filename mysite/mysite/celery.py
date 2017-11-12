import os
import django
from celery import Celery
from django.conf import settings
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# django.setup()
app = Celery('Tasks')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.timezone = settings.TIME_ZONE

@app.task(bind=True)
def debug_task(self):
    logging.info('request {0!r}'.format(self.request))
    # print('Request: {0!r}'.format(self.request))