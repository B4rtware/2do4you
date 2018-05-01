from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'todo/index.html', None)

def create(request):
    return render(request, 'todo/create.html', None)