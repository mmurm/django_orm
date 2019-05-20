from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt



def index(request):
    if 'id' not in request.session:
        return render(request, "wall/login.html", )
    else:
        return redirect( "/wall/wall" )


def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/wall/')
    else:
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],password=hash_pw)
        request.session['id'] = user.id
        request.session['f_name'] = user.first_name
        return redirect("/wall/")

def login(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['id']= user.id
        request.session['f_name'] = user.first_name
        return redirect("/wall/")

def wall(request):
    context={
        "all_users" : User.objects.all(),
        "all_messages" : Message.objects.all(),
        "all_comments" : Comment.objects.all(),
    }
    return render(request, "wall/index.html", context)

def post_message(request):
    user=User.objects.get(id=request.session['id'])
    Message.objects.create(user=user, message=request.POST['message'])
    return redirect("/wall/")

def post_comment(request):
    user=User.objects.get(id=request.session['id'])
    message=Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(message=message, user=user, comment=request.POST['comment'])
    return redirect("/wall/")



def logout(request):
    del request.session['id']
    return redirect("/wall/")

