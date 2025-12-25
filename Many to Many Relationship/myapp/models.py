from django.db import models
from django.contrib.auth.models import User


# Many to Many
class Song(models.Model):
    user = models.ManyToManyField(User)
    # user = models.ManyToManyField(User, on_delete=models.PROTECT)
    # user = models.ManyToManyField(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)

    def written_by(self):
        return ", ".join([str(p) for p in self.user.all()])
