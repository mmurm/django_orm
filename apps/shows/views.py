from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_shows" : Show.objects.all(),
    }
    return render(request, "shows/index.html", context )

def new(request):
    return render(request, "shows/new.html",)

def create(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], show_desc=request.POST['show_desc'])
    return redirect("/shows/",)

def view(request, id):
    context = {
        "show" : Show.objects.get(id=id),
    }
    return render(request, "shows/view.html", context )

def edit(request, id):
    context = {
        "show" : Show.objects.get(id=id),
    }
    return render(request, "shows/edit.html", context )

def update(request, id):
    show=Show.objects.get(id=id)
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.release=request.POST['release']
    show.show_desc=request.POST['show_desc']
    show.save()
    return redirect("/shows")

def delete(request, id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect("/shows")



# def index(request):
#     context = {
#         "all_dojos" : dojo.objects.all(),
#         "all_ninjas" : ninja.objects.all()
#     }
#     return render(request, "dojo_ninja/index.html", context )

# def process_dojo(request):
#     dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
#     return redirect("/dojo")# Create your views here.
