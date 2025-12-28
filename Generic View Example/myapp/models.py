from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
