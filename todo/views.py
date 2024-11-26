from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Todo

def index(request):
    return render(request, "index.html")

@csrf_exempt
def loginPost(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("todos")
    else:
        return redirect("loginfailed")

def loginfailed(request):
    return render(request, "loginfailed.html")

@login_required
def todoView(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, "mainview.html", {"todos": todos})

@login_required
@csrf_exempt
def addTodo(request):
    description = request.POST.get("description")
    Todo.objects.create(user=request.user, description=description, completed=False)
    return redirect("todos")
