from django.urls import path
from .views import Contacts, home, blog, about, blog_detail, GetAllBlogFromSingleCategory
urlpatterns = [
    path("", home, name="home"),
    path("blog", blog, name="blog"),
    path("post/<slug:slug>/", blog_detail, name="post"),
    path("about", about, name="about"),
    path("contact", Contacts, name="contact"),
    path("getSingleCategory/<int:id>/", GetAllBlogFromSingleCategory, name="getSingleCategory"),
]
