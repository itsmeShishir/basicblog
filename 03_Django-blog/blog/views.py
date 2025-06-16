from django.shortcuts import render, HttpResponse
from .models import Blog
from categorys.models import Category

# def home(request):
#     return HttpResponse("Hello World")

# Create your views here.
def home(request):
    isSlider = Blog.objects.filter(isSlider=True).order_by('-created_at')
    isFeatured = Blog.objects.filter(isFeatured=True).order_by('-created_at')
    isFeaturs = isFeatured[:1]
    category = Category.objects.filter(isShow=True).order_by('-id')
    fourCategory = category[:4]
    blog = Blog.objects.all().order_by('-created_at')
    fourBlog= blog[:4]
    context = {
        "isSlider": isSlider,
        "isFeaturs": isFeaturs,
        "fourCategory": fourCategory, 
        "fourBlog": fourBlog
    }
    return render(request, "index.html", context)

def blog_detail(request, slug): 
    post = Blog.objects.get(slug=slug)
    print(post)
    related = Blog.objects.filter(category=post.category).exclude(slug=slug)
    context = {
        "post": post,
        "related": related
    }
    return render(request, "post.html", {"context": context})


def blog(request):
    allblog = Blog.objects.all()
    return render(request, "blog.html", {"allblog": allblog})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")