from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Food(models.Model):
    food_name = models.CharField(max_length=255)
    food_description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_image = models.ImageField(
        upload_to="meals/images", default="meals/images/default.png"
    )

    def __str__(self):
        return self.food_name
