import sqlite3

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from tietoturpa.settings import DATABASES
from .models import Message, RecoveryAnswer


def index(request):
    messages = Message.objects.all()
    return render(request, "index.html", {"messages": messages})

def loginScreen(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "loginscreen.html")

def createUser(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "createuser.html")

def createUserPost(request):
    if request.user.is_authenticated:
        return redirect("index")

    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    dob = request.POST.get("dob")

    created = User.objects.create(username=username, password=password, email=email)
    login(request, created)
    RecoveryAnswer.objects.create(user=created, answer=dob)

    return redirect("index")

def forgotPassword(request):
    return render(request, "forgotpassword.html")

def forgotPasswordPost(request):
    username = request.POST.get("username")
    user = User.objects.get(username=username)
    # Insecure version
    user_dob = RecoveryAnswer.objects.get(user=user)

    given_dob = request.POST.get("dob")
    if user_dob.answer == given_dob:
        password = request.POST.get("password")
        user.set_password(password)
        user.save()
        return redirect("passwordchanged")
    # Insecure version ends
    # Secure version
    # Send a password recovery email (not going to implement because that is way too complicated)
    # Secure version ends

    return redirect("passwordnotchanged")

def passwordChanged(request):
    return render(request, "passwordchanged.html")

def passwordNotChanged(request):
    return render(request, "passwordnotchanged.html")

def loginPost(request):
    if request.user.is_authenticated:
        return redirect("index")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return redirect("loginfailed")

def loginFailed(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "loginfailed.html")

@login_required
def logOut(request):
    logout(request)
    return redirect("index")

# Uncomment for secure version
# @login_required
def adminScreen(request):
    allusers = User.objects.all()
    return render(request, "adminScreen.html", {"users": allusers})

# Remove line below for secure version
@csrf_exempt
def postMessage(request):
    if not request.user.is_authenticated:
        return redirect("index")

    messagetext = request.POST.get("message")

    # Insecure version
    query = f"INSERT INTO forum_message(user_id, message) VALUES ({request.user.id}, '{messagetext}');"
    database = DATABASES.get("default").get("NAME")
    conn = sqlite3.connect(database)
    with conn:
        conn.executescript(query)
    # Insecure version ends

    # Secure raw version
    # database = DATABASES.get("default").get("NAME")
    # query = f"INSERT INTO forum_message(user_id, message) VALUES (?, ?)"
    # conn = sqlite3.connect(database)
    # with conn:
    #     conn.execute(query, (request.user.id, messagetext))
    # Secure raw version ends

    # Secure version alt
    # Message.objects.create(user=request.user, message=messagetext)
    # Secure version ends

    return redirect("index")
