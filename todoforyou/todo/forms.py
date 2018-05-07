from django.forms import ModelForm, DateInput, TextInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["description", "deadline", "progress"]
        widgets = {
            "deadline": DateInput(attrs={'class': 'datepicker form-control'}),
            "description": TextInput(attrs={'class': 'form-control'}),
            "progress": TextInput(attrs={'class': 'form-control'})
        }