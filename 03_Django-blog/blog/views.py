from django.shortcuts import render, HttpResponse
from .models import Blog
from categorys.models import Category

# def home(request):
#     return HttpResponse("Hello World")

# Create your views here.
def home(request):
    isSlider = Blog.objects.filter(isSlider=True)
    isFeatured = Blog.objects.filter(isFeatured=True)
    category = Category.objects.all()
    context = {
        "isSlider": isSlider,
        "isFeatured": isFeatured,
        "category": category
    }
    return render(request, "index.html", context)

def blog(request):
    allblog = Blog.objects.all()
    return render(request, "blog.html", {"allblog": allblog})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")