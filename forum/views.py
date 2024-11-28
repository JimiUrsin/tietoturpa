from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction

from .models import Message

# Create your views here.
def index(request):
    messages = Message.objects.all()
    return render(request, "index.html", {"messages": messages})

def loginScreen(request):
    return render(request, "loginscreen.html")

def loginPost(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return redirect("loginfailed")

def loginFailed(request):
    return render(request, "loginfailed.html")

def logOut(request):
    logout(request)
    return redirect("index")

@csrf_exempt
def postMessage(request):
    if not request.user.is_authenticated:
        return redirect("index")

    messagetext = request.POST.get("message")
    query = f"INSERT INTO forum_message(user_id, message) VALUES ({request.user.id}, '{messagetext}');"

    print(query)

    with connection.cursor() as cursor:
        cursor.executemany(query, [])
        transaction.commit()

    return redirect("index")
