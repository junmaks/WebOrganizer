from django.shortcuts import render
from .models import CardTask
from datetime import datetime
from django.utils import timezone

# Create your views here.

def index(request):
    all_tasks = CardTask.objects.all()
    status_task = all_tasks.filter(task_status='Task')
    status_progress = all_tasks.filter(task_status='Progress')
    status_complete = all_tasks.filter(task_status='Complete')
    context = {
        'status_task': status_task,
        'status_progress': status_progress,
        'status_complete': status_complete,
    }
    return render(request=request, template_name='tasks/index.html', context=context)


def view_tasks(request):
    return render(request=request, template_name='tasks/view_tasks.html', context={})


def add_tasks(request):
    return render(request=request, template_name='tasks/add_view_task.html', context={})


def edit_tasks(request):
    return render(request=request, template_name='tasks/add_view_task.html', context={})
