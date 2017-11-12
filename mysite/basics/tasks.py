from celery import shared_task
import logging

from .models import Tag


@shared_task
def celery_app_test():
    logging.info('Test from iniside django app')
    a = Tag.objects.all()[:10]
    return [x.name for x in a]


@shared_task
def queue_test():
    logging.info('Different queue')
