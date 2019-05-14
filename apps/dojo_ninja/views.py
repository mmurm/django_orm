from django.shortcuts import render, redirect

def index(request):
    return render(request, "dojo_ninja/index.html" )

def process(request):
    return render(request, "dojo_ninja/index.html" )