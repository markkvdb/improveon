from django.db import models

from core.models import TimeStampedModel

# Create your models here.
class Company(TimeStampedModel):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    anonymous = models.BooleanField()

    def __str__(self):
        return self.name
