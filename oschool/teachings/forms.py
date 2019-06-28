from django import forms
from .models.lesson import Lesson


class LessonCreationForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'start_time', 'end_time', 'description', 'subject']
        widgets = {'start_time': forms.TimeInput(format='%H:%M'), 'end_time': forms.TimeInput(format='%H:%M')}
