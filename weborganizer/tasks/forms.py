from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError

from .models import CardTask
from django.contrib.admin import widgets


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = CardTask
        fields = ['title', 'text', 'time_start', 'time_end']
        # fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'description_card text-center', }),
            'text': forms.Textarea(attrs={'class': 'description_card', }),
            'time_start': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'description_card text-center'},
                format='%Y-%m-%dT%H:%M', ),
            'time_end': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'description_card text-center', },
                format='%Y-%m-%dT%H:%M'),
        }

    def clean_title(self):
        '''
        Прописываем свою валидацию. Название не должно начинаться с цифры
        :return:
        '''
        title = self.cleaned_data['title']
        if title is None:
            raise ValidationError('Укажите название')
        return title

    def clean_time_start(self):
        '''
        Прописываем свою валидацию. Время должно быть указано
        :return:
        '''
        time_start = self.cleaned_data['time_start']
        if time_start is None:
            raise ValidationError('Укажите дату начала')
        return time_start

    def clean_time_end(self):
        '''
        Прописываем свою валидацию. Время должно быть указано и должно быть больше
        времени начала
        :return:
        '''
        time_start = self.cleaned_data['time_start']
        time_end = self.cleaned_data['time_end']
        if time_end is None:
            raise ValidationError('Укажите дату завершения')
        if time_end < time_start and time_start is not None:
            raise ValidationError('Укажите корректную дату завершения')
        return time_end
