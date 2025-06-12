from django.contrib import admin
from .models import Blog, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

# python manage.py makemigrations blog
# python manage.py migrate

