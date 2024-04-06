from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name= "blogspost-view-create"),
    path("blogposts/<int:pk>/", views.BlogRetrieveUpdateDestroy.as_view(), name= "CRUD")
]
