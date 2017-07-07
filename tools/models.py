from django.db import models

from students.models import Student

# Create your models here.
class Tool(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    downloads = models.IntegerField(default=0)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
