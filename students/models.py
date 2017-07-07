from django.db import models

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    email = models.EmailField(default="default@email.com")
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name