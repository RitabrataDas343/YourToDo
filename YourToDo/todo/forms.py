from django import forms
from django.forms import ModelForm
from .models import ToDo

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['task']

        widgets = {
            'task': forms.TextInput(attrs= {'class': 'addTask', 'placeholder': 'Type your task !'})
        }