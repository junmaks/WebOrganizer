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
            print(True)
        if time_now > item.time_start and time_now > item.time_end:
            item.task_status = 'Complete'
            item.save()

    # while True:
    #     all_tasks = CardTask.objects.all()
    #     first_card = all_tasks.get(pk=1)
    #     print(first_card.time_start, first_card.time_end, )
    #     a = datetime.now()
    #     a = a.strftime("%Y-%m-%d %H:%M:%S+00:00")
    #     b = first_card.time_start.strftime("%Y-%m-%d %H:%M:%S+00:00")
    #     print(a<b)
    #     print(b)
    #     print(a)
    #     print(type(first_card.time_start))
    #     print(type(a))

    # status_task = all_tasks.filter(task_status='Task')
    # for item in status_task:
    #     if item
    #
    # status_progress = all_tasks.filter(task_status='Progress')



# @shared_task
# def add(x, y):
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)

#
# @shared_task
# def count_widgets():
#     return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()