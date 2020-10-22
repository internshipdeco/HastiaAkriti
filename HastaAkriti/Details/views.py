from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,"website.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def details(request):
    return render(request,"details.html")

def properties(request):
    return render(request,"properties.html")

def services(request):
    return render(request,"services.html")

def news(request):
    return render(request,"news.html")