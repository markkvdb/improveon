from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel


# Create your models here.
class Company(TimeStampedModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.name
