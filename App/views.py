from datetime import datetime
from email import message
import http
from logging import exception
import profile
import re
from django.shortcuts import redirect, render,HttpResponse
from App.models import Contact,Profile,Pick
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import uuid 
from django.db import models
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
 
    context={
        "variable":"hello"
    }
    
    return render(request,"homepage.html",context)

def Info(request):
    if request.user.is_anonymous:
      messages.success(request,"Please Log-in first")
      return redirect("/Login")
    else:
     return render(request,"Information.html")


def contact(request):
 if request.user.is_anonymous:
      messages.success(request,"Please Log-in first")
      return redirect("/Login")
 else:
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        contact=Contact(name=name,email=email,feedback=feedback,date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you for giving  your feedback')

    return render(request,"Contact.html")

def About(request):
    if request.user.is_anonymous:
      messages.success(request,"Please Log-in first")
      return redirect("/Login")
    else:
      return render(request,"About.html")

def Login(request):
    

    if request.method=="POST":
        print("hello")
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        profile_obj=Profile.objects.filter(user=user_obj).first()



        if not profile_obj.is_verified:
            messages.success(request,"You are not verified")
            return redirect("/Login")
        
        user=authenticate(username=username,password=password)
        
        if user is not None :
            login(request,user)
            return redirect("/")
        else:
            return redirect("/Login")
    return render(request,"loginpage.html")

def Signup(request):
    if request.method=="POST":
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")
        print(password)


        if User.objects.filter(username=username).first():
            messages.success(request,"User name is taken")
            return redirect("/Signup")

        if password!=repassword:
            messages.success(request,"Please enter the correct Password")
            return redirect("/Signup")

        if User.objects.filter(email=email).first():
            messages.success(request,"Email is taken")
            return  redirect("/Signup")
        
        user_obj=User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        
        
        token=str(uuid.uuid4())
        Pick.objects.create(user=user_obj)
        profile_obj=Profile.objects.create(user=user_obj,auth_token=token)
        profile_obj.save()
        send_mail_after(email,token)
        
        messages.success(request,"mesage has been sent to your email")


    return render(request,"Signuppage.html")

def Logout_user(request):
    logout(request)
    return redirect("/Login")

def send_mail_after(email,token):
    subject="YOur Accounts need to be verified"
    messages=f"hii.This is link for verfication http://127.0.0.1:8000/verify/{token}"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,messages,email_from,recipient_list)

def verify(request,auth_token):
    profile_obj=Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        profile_obj.is_verified=True
        profile_obj.save()
      
        messages.success(request," You are verified")
        return redirect("/")
    
def change_password(request,forgot_token):
    if  not Pick.objects.filter(forgot_token=forgot_token).first():
        return redirect("/Login")
    messages.success(request,"You can now change password")
    return redirect("/pc")
    

def Pc(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")

        if password!=repassword:
            return redirect("/Pc")
        user_obj=User.objects.get(username=username)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,"Your password has been changed")
        return redirect("/Login")



    return render(request,"pc.html")



def Forgot(request):

    if request.method=="POST":
        print("hello")
        username=request.POST.get("username")

        if not User.objects.filter(username=username).first():
           messages.success(request,"You are not registered")
           return redirect("/Signup")
        else:
            print("hello")
            user_obj=User.objects.get(username=username)
            email=user_obj.email
            token=str(uuid.uuid4())
            Pick_obj=Pick.objects.get(user=user_obj)
            Pick_obj.forgot_token=token
            
            Pick_obj.save()

            Forgotpassword_mail(email,token)
            messages.success(request,"message has been sent")
        
       
    return render(request,"forgotpassword.html")


def Forgotpassword_mail(email,token):
    print(email,token)
    subject="this is a link to change password"
    messages=f"hii.This is link for verfication http://127.0.0.1:8000/Changepassword/{token}"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,messages,email_from,recipient_list)
