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

class TodoIndexView(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        queryset = super(TodoIndexView, self).get_queryset()
        return queryset.filter(user_id = self.request.user)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)

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