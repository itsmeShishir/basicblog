from django.urls import path
from .views import Contacts, home, blog, about, blog_detail, GetAllBlogFromSingleCategory, blog_api, BlogList
urlpatterns = [
    path("", home, name="home"),
    path("blog", blog, name="blog"),
    path("post/<slug:slug>/", blog_detail, name="post"),
    path("about", about, name="about"),
    path("contact", Contacts, name="contact"),
    path("getSingleCategory/<int:id>/", GetAllBlogFromSingleCategory, name="getSingleCategory"),
    path("api/blog", blog_api, name="blog_api"),
    path("api/BlogList", BlogList.as_view(), name="BlogList"),
]
