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
    all_objects = models.Manager() # tout

    def __str__(self):
        return self.name
    
class Experiences(SoftDeleteModel):
    job_title = models.CharField(max_length=500)
    entreprise_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    current_job = models.BooleanField(default=False)
    description = models.TextField()

    objects = SoftDeleteManager() ## seulement actif
    all_objects = models.Manager() # tout

    def __str__(self):
        return self.description

class Certifications(SoftDeleteModel):
    name = models.CharField(max_length=200)
    organisme = models.CharField(max_length=200)
    obtaining_date = models.DateField()

    objects = SoftDeleteManager() ## seulement actif
    all_objects = models.Manager() # tout

    def __str__(self):
        return self.description