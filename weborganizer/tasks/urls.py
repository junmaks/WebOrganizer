from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('view/<view_title>', view_tasks, name='view'),
    path('add/', add_tasks, name='add'),
    path('edit/<view_title>/<int:task_id>', edit_tasks, name='edit'),
]