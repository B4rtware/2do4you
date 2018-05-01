from .forms import TodoForm
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'todo/index.html', None)

def create(request):
    if request.method == 'POST':
        pass
    else:
        form = TodoForm()
        content = {"form": form}
    return render(request, 'todo/create.html', content)