from django.contrib import admin
from .models import Profile, Post, Song


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city", "user"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user"]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["title"]
