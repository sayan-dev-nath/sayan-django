from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField(unique=True, null=True)
    course = models.CharField(max_length=255)
