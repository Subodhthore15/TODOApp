from django import forms
from django.db.models import fields

from todoapp.models import Mytodo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task',]