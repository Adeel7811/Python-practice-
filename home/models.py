from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    rollno = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)