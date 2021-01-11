from django.db import models
from . import managers


# Create your models here.
class Time_stamped_Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True  # So that this model is not in DB
        