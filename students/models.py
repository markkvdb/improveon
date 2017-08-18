from django.db import models
from django.contrib.auth.models import User
from core.signals import create_student
from django.dispatch import receiver


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=1000, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    resume = models.FileField(null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


def update_user_student(sender, **kwargs):
    instance = kwargs['instance']
    Student.objects.create(user=instance)
    instance.student.save()

create_student.connect(update_user_student)
