from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from core.models import TimeStampedModel
from core.signals import create_company

# Create your models here.
class Company(TimeStampedModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    bio = models.CharField(max_length=1000, blank=True)
    likes = models.IntegerField(default=0)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'


@receiver(create_company, sender=User)
def update_user_company(sender, **kwargs):
    instance = kwargs['instance']
    Company.objects.create(user=instance)
    instance.company.save()