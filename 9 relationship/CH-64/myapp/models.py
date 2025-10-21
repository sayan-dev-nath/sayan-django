from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Song(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=255)
