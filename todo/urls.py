from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginPost, name="login"),
    path("loginfailed", views.loginfailed, name="loginfailed"),
    path("todos", views.todoView, name="todos"),
    path("addtodo", views.addTodo, name="addtodo"),
]
