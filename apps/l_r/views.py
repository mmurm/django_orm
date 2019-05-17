from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt



def index(request):
    
    return render(request, "l_r/index.html", )

def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/l_r/')
    else:
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],password=hash_pw)

        request.session['greeting'] = request.POST['first_name']
        return redirect("/l_r/success")

def login(request):
    errors = User.objects.login_validation(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/l_r/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['greeting']= user.first_name
        print(user.first_name)
        return redirect("/l_r/success")
    

def success(request):
    return render(request, "l_r/success.html", )

def logout(request):
    return redirect("/l_r/")

