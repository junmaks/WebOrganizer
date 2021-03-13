from django.shortcuts import render, redirect, get_object_or_404
from .models import CardTask
from .forms import AddTaskForm
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
    status_complete = CardTask.objects.filter(task_status=view_title)
    context = {
        'status': status_complete,
        'view_title': view_title
    }
    return render(request=request, template_name='tasks/view_tasks.html', context=context)


def add_tasks(request):
    status_task = CardTask.objects.filter(task_status='Task')

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddTaskForm()
    context = {
        'status_task': status_task,
        'form': form,
    }
    return render(request=request, template_name='tasks/add_view_task.html', context=context)


def edit_tasks(request, view_title, task_id):
    status_task = CardTask.objects.filter(task_status=view_title)
    task = get_object_or_404(CardTask, pk=task_id)
    form = AddTaskForm(request.POST, instance=task)
    if request.method == 'POST' and 'edit_task.x' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    elif request.method == 'POST' and 'complete_task.x' in request.POST:
        task.time_end = timezone.now()
        task.task_status = 'Complete'
        task.save()
        return redirect('home')
    elif request.method == 'POST' and 'delete_task.x' in request.POST:
        task.delete()
        return redirect('home')
    else:
        form = AddTaskForm(instance=task)
    context = {
        'view_title': view_title,
        'status_task': status_task,
        'form': form,
        'task_id': task_id,
    }
    return render(request=request, template_name='tasks/edit_task.html', context=context)
