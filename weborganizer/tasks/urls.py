from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('view/', view_tasks, name='view'),
    path('add/', add_tasks, name='add'),
    path('edit/', edit_tasks, name='edit'),

]