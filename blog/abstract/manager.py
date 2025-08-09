from django.db import models

class SoftDeleteManager(models.Manager):
    def get_queryset(self):

        # Filtre les objets supprimés
        return super().get_queryset().filter(is_deleted=False)
