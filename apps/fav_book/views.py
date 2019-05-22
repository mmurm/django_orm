from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt



def index(request):
    if 'id' not in request.session:
        return render(request, "fav_book/login.html", )
    else:
        return redirect( "/fav_b/books" )


def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/fav_b/')
    else:
        hash_pw = bcrypt.hashpw(request.POST['r_password'].encode(),bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['r_email'],password=hash_pw)
        request.session['id'] = user.id
        request.session['f_name'] = user.first_name
        return redirect("/fav_b/")

def login(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/fav_b/')
    else:
        user = User.objects.get(email=request.POST['l_email'])
        request.session['id']= user.id
        request.session['f_name'] = user.first_name
        return redirect("/fav_b/")

def books(request):
    context={
        "user" : User.objects.get(id=request.session['id']),
        "all_books" : Book.objects.all(),
    }
    return render(request, "fav_book/books.html", context)

def book(request, book_id):
    context={
        "all_users" : User.objects.all(),
        "this_user" : User.objects.get(id=request.session['id']),
        "book" : Book.objects.get(id=(book_id)),
        "all_likes" : User.objects.filter(user_like=(book_id))
    }
    
    return render(request, "fav_book/book.html", context)

def add_book(request):
    user=User.objects.get(id=request.session['id'])
    book=Book.objects.create(title=request.POST['title'], book_desc=request.POST['book_desc'], upload=user)
    book.like.add(user)
    book.save()
    return redirect("/fav_b/")

def add_to_fav(request, book_id):
    user=User.objects.get(id=request.session['id'])
    book=Book.objects.get(id=(book_id))
    book.like.add(user)
    book.save()
    return redirect("/fav_b/")

def delete(request, book_id):
    this_book=Book.objects.get(id=(book_id))
    this_user=User.objects.get(id=request.session['id'])
    this_user.user_like.remove(this_book)
    return redirect("/fav_b/")

def logout(request):
    del request.session['id']
    return redirect("/fav_b/")

