from django import views
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    
    path("",views.homepage,name="home"),
    path("Information",views.Info,name="info"),
    path("Contact",views.contact,name="Conta"),
    path("About",views.About,name="Abo"),
    path("Login",views.Login,name="login"),
    path("Signup",views.Signup,name="signup"),
    path("logout",views.Logout_user,name="logout"),
    path("verify/<auth_token>",views.verify,name="verify"),
    path("Changepassword/<forgot_token>",views.change_password,name="chang"),
    path("Forgot",views.Forgot,name="forgot"),
    path("pc",views.Pc,name="pc"),
    
]