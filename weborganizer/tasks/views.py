from django.shortcuts import render, redirect
from .models import CardTask
from .forms import AddTaskForm
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


def view_tasks(request, view_title):
    if view_title == 'Task':
        status_task = CardTask.objects.filter(task_status='Task')
        context = {
            'status': status_task,
            'view_title': view_title
        }
    if view_title == 'Progress':
        status_progress = CardTask.objects.filter(task_status='Progress')
        context = {
            'status': status_progress,
            'view_title': view_title
        }
    if view_title == 'Complete':
        status_complete = CardTask.objects.filter(task_status='Complete')
        context = {
            'status': status_complete,
            'view_title': view_title
        }

    return render(request=request, template_name='tasks/view_tasks.html', context=context)


def add_tasks(request):
    status_task = CardTask.objects.filter(task_status='Task')

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            card_task = form.save()
            return redirect(card_task)
    else:
        form = AddTaskForm()
    context = {
        'status_task': status_task,
        'form': form,
    }
    return render(request=request, template_name='tasks/add_view_task.html', context=context)


def edit_tasks(request):
    return render(request=request, template_name='tasks/add_view_task.html', context={})
