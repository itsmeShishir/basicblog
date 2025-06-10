from django.db import models
from authenticationss.models import User

# Create your models here.
# ORM
# Object Relational Mapping -> oop to database
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey("categorys.Category", on_delete=models.CASCADE, 
                                 null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name