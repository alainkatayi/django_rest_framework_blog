from django.db import models

from articles.models import Categories

# Create your models here.

class Skills(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='skills')
    name= models.TextField()
    created_at = models.DateTimeField(auto_now=True)