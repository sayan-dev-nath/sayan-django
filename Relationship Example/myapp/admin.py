from django.contrib import admin
from .models import Page, Post, Song


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "publish", "user"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "publish", "user"]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "duration", "written_by"]
