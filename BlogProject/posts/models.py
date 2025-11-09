from django.db import models
from categories.models import Category
from authors.models import Author


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_category = models.ManyToManyField(Category)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
