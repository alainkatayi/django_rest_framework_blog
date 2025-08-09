from django.db import models

from abstract.base import SoftDeleteModel
from abstract.manager import SoftDeleteManager
from articles.models import Categories

# Create your models here.

class Skills(SoftDeleteModel):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='skills')
    name= models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    objects = SoftDeleteManager() ## seulement actif
    all_object = models.Manager() # tout

    def __str__(self):
        return self.name
