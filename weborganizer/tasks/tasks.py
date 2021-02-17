from django.utils import timezone
from celery import shared_task
# from demoapp.models import Widget
from .models import CardTask


@shared_task
def check_time():
    all_tasks = CardTask.objects.all()
    time_now = timezone.now()
    for item in all_tasks:
        if time_now > item.time_start and time_now < item.time_end:
            item.task_status = 'Progress'
            item.save()

