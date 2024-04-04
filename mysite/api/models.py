from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
class BlogPost(models.Model):
     title =  models.CharField(max_length = 60) 
     content = models.TextField()
     published_date = models.DateTimeField(auto_now  = TRUE)
     author = models.CharField(max_length = 60)
     
     def __str__(self) :
          return self.title
