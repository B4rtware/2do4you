from todo.forms import TodoForm, TodoSignupForm
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy

from todo.models import Todo

# Create your views here.

#def index(request):
#    todos = Todo.objects.all()#order_by('-importance')
#    payload = {"todos": todos}
#    return render(request, 'todo/index.html', payload)

class TodoIndexView(LoginRequiredMixin, ListView):
    model = Todo

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_update_form.html"
    success_url = reverse_lazy('index')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('index')
    
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_create_form.html"
    success_url = reverse_lazy('index')

class TodoSignupView(CreateView):
    form_class = TodoSignupForm
    success_url = reverse_lazy('index')
    template_name = "todo/todo_signup_form.html"

    def form_valid(self, form):
        valid = super(TodoSignupView, self).form_valid(form)

        if valid:
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            new_user = authenticate(username = username, password = password)

            if new_user:
                login(self.request, new_user)

        return valid

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))

def impressum(request):
    return render(request, 'todo/impressum.html', {})

def contact(request):
    return render(request, 'todo/contact.html', {})
    

def create(request):
    if request.is_ajax():
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save()
            data = {"message": "A new todo with id: {0} was successfully added!".format(new_todo.id)}
            return JsonResponse(data)
        else:
            data = {"message": "form is not valid!"}
            return JsonResponse(data)

    elif request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = TodoForm(request.POST)
        # check whether its valid
        if form.is_valid():
            description = form.cleaned_data.get("description")
            deadline = form.cleaned_data.get("deadline")
            progress = form.cleaned_data.get("progress")

            new_todo = Todo(description = description, deadline = deadline, progress = progress)
            new_todo.save()

            return HttpResponseRedirect(reverse_lazy('index'))
    else:
        form = TodoForm()
        return render(request, 'todo/create.html', {"form": form})