from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginscreen", views.loginScreen, name="loginscreen"),
    path("loginpost", views.loginPost, name="loginpost"),
    path("loginfailed", views.loginFailed, name="loginfailed"),
    path("logout", views.logOut, name="logout"),
    path("postmessage", views.postMessage, name="postmessage"),
    path("adminscreen", views.adminScreen, name="adminscreen"),
    path("createuser", views.createUser, name="createuser"),
    path("createuserpost", views.createUserPost, name="createuserpost"),
    path("forgotpassword", views.forgotPassword, name="forgotpassword"),
    path("forgotpasswordpost", views.forgotPasswordPost, name="forgotpasswordpost"),
    path("passwordchanged", views.passwordChanged, name="passwordchanged"),
    path("passwordnotchanged", views.passwordNotChanged, name="passwordnotchanged"),
]
