from django.db import models
from authenticationss.models import User

# Create your models here.
# ORM
# Object Relational Mapping -> oop to database
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey("categorys.Category", on_delete=models.CASCADE, 
                                 null=True, blank=True)
    isSlider = models.BooleanField(default=False)
    isFeatured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # slug auto generate form title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
        super().save(*args, **kwargs)
    
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