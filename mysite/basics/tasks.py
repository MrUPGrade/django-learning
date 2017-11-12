from celery import shared_task
import logging

from .models import Tag


@shared_task(bind=True)
def celery_app_test(self):
    logging.info('Test from iniside django app')
    logging.info('Request {0!r}'.format(self.request))
    a = Tag.objects.all()[:10]
    return [x.name for x in a]
