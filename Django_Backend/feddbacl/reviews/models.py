from django.db import models
from django.forms import CharField

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=50)
    review_text = models.TextField()
    rating = models.IntegerField()
    #owner_comment 
