from django.forms import ModelForm, DateInput, TextInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import Todo, TodoUser


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["description", "deadline", "progress", "importance"]
        widgets = {
            "deadline": DateInput(attrs={'class': 'datepicker form-control'}),
            "description": TextInput(attrs={'class': 'form-control'}),
            "progress": TextInput(attrs={'class': 'form-control'})
        }

class TodoAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["class"] = "form-control"

class TodoSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = TodoUser
    