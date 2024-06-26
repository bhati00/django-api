from django.shortcuts import render
from rest_framework import generics, response, status
from .models import BlogPost
from .serializations import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return response.Response(status= status.HTTP_204_NO_CONTENT)
    
class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView) :
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"