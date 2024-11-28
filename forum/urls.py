from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginscreen", views.loginScreen, name="loginscreen"),
    path("loginpost", views.loginPost, name="loginpost"),
    path("loginfailed", views.loginFailed, name="loginfailed"),
    path("logout", views.logOut, name="logout"),
    path("postmessage", views.postMessage, name="postmessage"),
]
