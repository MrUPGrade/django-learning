from django.shortcuts import render

from mysite.celery import debug_task
from .. import tasks

def celery_test(request):

    # result = debug_task.delay()
    result = tasks.celery_app_test.delay()
    tags = result.get()

    return render(request, 'basics/tasks/test.html', {'tags': tags})