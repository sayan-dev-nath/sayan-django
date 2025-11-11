from django.contrib import admin
from .models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "category_slug"]
    prepopulated_fields = {"category_slug": ("category_name",)}
