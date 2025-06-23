from django.urls import path
from .views import Contacts, home, blog, about, blog_detail, GetAllBlogFromSingleCategory, blog_api, BlogList, BlogCreate, BlogRetrive, BlogUpdate, BlogDelete
urlpatterns = [
    path("", home, name="home"),
    path("blog", blog, name="blog"),
    path("post/<slug:slug>/", blog_detail, name="post"),
    path("about", about, name="about"),
    path("contact", Contacts, name="contact"),
    path("getSingleCategory/<int:id>/", GetAllBlogFromSingleCategory, name="getSingleCategory"),
    path("api/blog", blog_api, name="blog_api"),
    path("api/BlogList", BlogList.as_view(), name="BlogList"),
    path("api/BlogCreate/", BlogCreate.as_view(), name="BlogCreate"), 
    path("api/getSingleBlog/<int:pk>/", BlogRetrive.as_view(), name="BlogCreate"), 
    path("api/updateSingleBlog/<int:pk>/", BlogUpdate.as_view(), name="BlogCreate"), 
    path("api/deleteSingleBlog/<int:pk>/", BlogDelete.as_view(), name="BlogCreate")
]
