from django.db import models
from abstract.base import SoftDeleteModel
from abstract.manager import SoftDeleteManager
from articles.models import Categories
from profiles.models import Skills

# Create your models here.
class Projects(SoftDeleteModel):
    name = models.TextField()
    description = models.TextField()
    created_at = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='projects')
    status = models.BooleanField(default=False)
    technology = models.ManyToManyField(Skills, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()
    

    def __str__(self):
        return self.name