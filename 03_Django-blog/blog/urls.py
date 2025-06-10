from django.urls import path
from .views import home, blog, about, contact
urlpatterns = [
    path("", home, name="home"),
    path("blog", blog, name="blog"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
]
