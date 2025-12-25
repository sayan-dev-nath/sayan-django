from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admission_date = models.DateTimeField()
