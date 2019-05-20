from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_books" : Book.objects.all(),
    }
    return render(request, "books_author/books.html", context )

def authors(request):
    context = {
        "all_authors" : Author.objects.all(),
    }
    return render(request, "books_author/authors.html", context )

def book(request, book_id):
    context = {
        "book" : Book.objects.get(id=book_id),
        "all_authors" : Author.objects.all(),
    }
    return render(request, "books_author/book.html", context )

def author(request, author_id):
    context = {
        "all_books" : Book.objects.all(),
        "all_authors" : Author.objects.all(),
    }
    return render(request, "books_author/author.html", context)

def process_book(request):
    Book.objects.create(title=request.POST['title'], book_desc=request.POST['book_desc'])
    return redirect("/b_a")

def process_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], note=request.POST['note'])
    return redirect("/b_a/authors")

def update_book(request, b_id):
    book=Book.objects.get(id=b_id)
    author=(request.POST['id'])
    book.authors.add(author)
    return redirect("/b_a/")

def update_author(request, a_id):
    author=Author.objects.get(id=a_id)
    book=(request.POST['id'])
    author.books.add(book)
    return redirect("/b_a/")
