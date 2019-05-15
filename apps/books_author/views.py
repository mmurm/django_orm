from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_books" : books.objects.all(),
    }
    return render(request, "books_author/books.html", context )

def book(request, book_id)
    pass

def author(request, author_id)
    pass

def authors(request):
    context = {
        "all_authors" : authors.objects.all()
    }
    return render(request, "books_author/books.html", context )


def process_book(request):
    books.objects.create(title=request.POST['title'], description=request.POST['description'], state=request.POST['state'])
    return redirect("/b_a")

def process_author(request):
    ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo.objects.get(id=request.POST['id']))
    return redirect("/b_a")