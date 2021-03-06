from django.shortcuts import render

from .. import tasks


def celery_test(request):
    tasks.queue_test.delay()

    result = tasks.celery_app_test.delay()
    tags = result.get()

    return render(request, 'basics/tasks/test.html', {'tags': tags})
