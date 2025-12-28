from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Page Title", max_length=255)
    category = models.CharField("Page Category", max_length=255)
    publish = models.DateField("Page Published Date")


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Post Title", max_length=255)
    category = models.CharField("Post Category", max_length=255)
    publish = models.DateField("Post Published Date")


class Song(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField("Song Title", max_length=255)
    duration = models.IntegerField("Song Duration")

    def written_by(self):
        return ", ".join([str(p) for p in self.user.all()])
