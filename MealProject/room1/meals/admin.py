from django.contrib import admin
from .models import Category, Food


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
    search_fields = ("category_name",)
    ordering = ("id",)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "food_name", "food_description")
    search_fields = ("food_name", "category__category_name")
    ordering = ("id",)
