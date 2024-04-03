from dataclasses import fields
from rest_framework import serializers

from mysite.api.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'