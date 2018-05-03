from todo.forms import TodoForm
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from todo.models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    payload = {"todos": todos}
    return render(request, 'todo/index.html', payload)


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')

def create(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = TodoForm(request.POST)
        # check whether its valid
        if form.is_valid():
            description = form.cleaned_data.get("description")
            deadline = form.cleaned_data.get("deadline")
            progress = form.cleaned_data.get("progress")

            new_todo = Todo(description = description, deadline = deadline, progress = progress)
            new_todo.save()

            return HttpResponseRedirect('/todo/')
    else:
        form = TodoForm()
        return render(request, 'todo/create.html', {"form": form})