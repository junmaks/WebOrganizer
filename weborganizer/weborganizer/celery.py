import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weborganizer.settings')

app = Celery('weborganizer')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'check_time':
        {
            'task': 'tasks.tasks.check_time',
            'schedule': 10.0,
        }
}