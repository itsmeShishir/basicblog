from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Blog, Comment, Contact
from categorys.models import Category
from .forms import CommentForm
from django.contrib import messages
from .serializations import BlogSerialization, BlogCreateRetriveSerialization
from rest_framework import generics

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
    blog = get_object_or_404(Blog, slug=slug)
    related_Blog = Blog.objects.filter(category=blog.category).exclude(slug=slug)[:3]
    commets = Comment.objects.filter(blog=blog).order_by('-created_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect("post", slug=slug)
    else:
        form = CommentForm()
    context = {
        "blog": blog,
        "related_Blog": related_Blog,
        "commets": commets,
        "form": form
    }
    return render(request, "post.html", context)


def blog(request):
    allblog = Blog.objects.all()
    return render(request, "blog.html", {"allblog": allblog})


def GetAllBlogFromSingleCategory(request, id):
    category = get_object_or_404(Category, id=id)
    allblog = Blog.objects.filter(category=category)
    return render(request, "onlyCategoryBlog.html", {"allblog": allblog})

def about(request):
    return render(request, "about.html")

def Contacts(request):
    if request.method =="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
       
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Message send successfully")
        return redirect("home")
    return render(request, "contact.html")



def blog_api(request):
    blog = Blog.objects.all()
    serializer = BlogSerialization(blog, many=True)
    return HttpResponse(serializer.data)

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialization


class BlogCreate(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateRetriveSerialization

class BlogRetrive(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    lookup = "pk"
    serializer_class = BlogSerialization

class BlogUpdate(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    lookup = "pk"
    serializer_class = BlogCreateRetriveSerialization

class BlogDelete(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    lookup = "pk"
    serializer_class = BlogCreateRetriveSerialization