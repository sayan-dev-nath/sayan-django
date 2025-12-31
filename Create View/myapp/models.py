from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("create")  # pattern_name = create
