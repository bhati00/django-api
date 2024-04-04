from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializations import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serialzer_class = BlogPostSerializer