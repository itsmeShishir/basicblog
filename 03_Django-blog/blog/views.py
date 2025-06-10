from django.shortcuts import render, HttpResponse
from .models import Blog

# def home(request):
#     return HttpResponse("Hello World")

# Create your views here.
def home(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")