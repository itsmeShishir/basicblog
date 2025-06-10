from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    isShow = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to= "category/", null=True, blank=True)

    def __str__(self):
        return self.name
    
# python manage.py makemigrations
# python manage.py migrate