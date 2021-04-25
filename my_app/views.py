from django.shortcuts import render, redirect
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'my_app/index.html', {'tasks': tasks})


def add_task(request):
    Task.objects.create(title=request.POST['content'])
    return redirect('index')
