from django.db import models
from authors.models import Author


# Create your models here.
class Profile(models.Model):
    profile_name = models.CharField(max_length=255)
    profile_about = models.TextField()
    profile_author = models.OneToOneField(
        Author, on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.profile_name
