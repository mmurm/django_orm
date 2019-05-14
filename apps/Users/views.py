from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        "all_users" : user.objects.all()
    }
    return render(request,'users/index.html', context)

def process(request):
    user.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    return redirect('/users')
