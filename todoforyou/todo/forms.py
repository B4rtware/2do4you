from django.forms import ModelForm, DateInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["description", "deadline", "progress"]
        widgets = {
            "deadline": DateInput(attrs={'class': 'datepicker'}),
        }