from django.db import models

from core.models import TimeStampedModel
from companies.models import Company

# Create your models here.
class Job(TimeStampedModel):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name