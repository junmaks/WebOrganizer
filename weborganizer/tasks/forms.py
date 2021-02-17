from django import forms
from .models import CardTask


class AddTaskForm(forms.ModelForm):

    class Meta:
        model = CardTask
        fields ='__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'description_card text-center',}),
            'text': forms.Textarea(attrs={'class': 'description_card', }),
            'time_start': forms.TextInput(attrs={'type': 'datetime-local', 'class': 'description_card'}),
            'time_end': forms.TextInput(attrs={'type': 'date', 'class': 'description_card'}),

        }
