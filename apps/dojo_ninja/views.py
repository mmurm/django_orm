from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_dojos" : dojo.objects.all(),
        "all_ninjas" : ninja.objects.all()
    }
    return render(request, "dojo_ninja/index.html", context )

def process_dojo(request):
    dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect("/dojo")

def process_ninja(request):
    ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo.objects.get(id=request.POST['id']))
    return redirect("/dojo")