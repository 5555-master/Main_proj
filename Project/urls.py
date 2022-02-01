"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("App.urls")),
    path("Information",include("App.urls")),
    path("Contact",include("App.urls")),
    path("About",include("App.urls")),
    path("Login",include("App.urls")),
    path("Signup",include("App.urls")),
    path("logout",include("App.urls")),
    path("token",include("App.urls")),
    path("verify/<auth_token>",include("App.urls")),
    path("Changepassword/<forgot_token>",include("App.urls")),
    path("Forgot",include("App.urls")),
    path("pc",include("App.urls")),
]

admin.site.site_header = "Plants Admin"
admin.site.site_title = "Plants Admin Portal"
admin.site.index_title = "Welcome to Plants Admin Portal"