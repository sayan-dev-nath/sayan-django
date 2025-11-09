from django.contrib import admin
from .models import Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["author_name", "author_bio", "author_phone"]
