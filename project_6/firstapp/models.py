from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()

    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"
