from rest_framework import serializers
from .models import Blog

class BlogSerialization(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'category', 'isSlider', 'isFeatured', 'user', 'image', 'created_at', 'updated_at']

class BlogCreateRetriveSerialization(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'category', 'isSlider', 'isFeatured', 'user', 'image', 'created_at', 'updated_at']