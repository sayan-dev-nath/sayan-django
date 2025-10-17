from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name


class Result(models.Model):
    cls = models.CharField(max_length=50)
    marks = models.IntegerField()

    # def __str__(self):
    #     return self.cls
