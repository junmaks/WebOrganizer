from django.db import models

# Create your models here.
from django.urls import reverse


class CardTask(models.Model):

    statuses = [('Task', 'Task'), ('Progress', 'Progress'), ('Complete', 'Complete'), ('Deleted', 'Deleted')]

    title = models.CharField(verbose_name='Заголовок', max_length=150,)
    text = models.TextField(verbose_name='Описание задачи', blank=True, )
    time_start = models.DateTimeField(verbose_name='Начало',)
    time_end = models.DateTimeField(verbose_name='Завершение',)
    task_status = models.CharField(verbose_name='Статус выполнения', max_length=8, default='Task', choices=statuses)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('edit', kwargs={'task_id': self.pk})

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['time_start']