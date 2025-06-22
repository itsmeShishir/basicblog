from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Blog, Contact
from categorys.models import Category

# Create your views here.

User = get_user_model()

def register_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        profile_image = request.FILES.get("profile_image")
        phone_number = request.POST["phone_number"]

        if password != confirm_password:
            messages.error(request, "password doesnot match")
            return redirect("register")
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "email already exists")
            return redirect("register")
        
        if User.objects.filter(username = username).exists():
            messages.error(request, "username already exists")
            return redirect("register")
        
        user = User.objects.create_user(
            username=username,
            full_name=full_name,
            email=email,
            password=password,
            profile_image=profile_image,
            phone_number=phone_number
        )
        messages.success(request, "account created successfully")
        return redirect("login")
    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "logged in successfully")
            return redirect("home")
        else:
            messages.error(request, "invalid credentials")
            return redirect("login")
    return render(request, "login.html")

def logouts(request):
    logout(request)
    return redirect("logins")

# @login_required(login_url="login") -> decorator -> update password , updatae profile 
@login_required(login_url="login")
def update_password(request):
    return render(request, "update_password.html")

@login_required(login_url="login")
def update_profile(request):
    return render(request, "update_profile.html")

@login_required(login_url="login")
def dashboard(request):
    contact = Contact.objects.all()
    blog = Blog.objects.all()
    category = Category.objects.all()
    print(contact)
    context = {
        "contact": contact,
        "blog": blog,
        "category": category
    }
    return render(request, "dashboard.html", context)    

@login_required(login_url="login")
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    messages.success(request, "contact deleted successfully")
    return redirect("dashboard")


@login_required(login_url="login")
def update_contact(request, id):    
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.name = request.POST["name"]
        contact.email = request.POST["email"]
        contact.subject = request.POST["subject"]
        contact.message = request.POST["message"]
        contact.save()
        messages.success(request, "contact updated successfully")
        return redirect("dashboard")
    return render(request, "updateContact.html", {"contact": contact})