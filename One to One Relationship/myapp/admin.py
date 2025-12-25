from django.contrib import admin
from .models import Profile, Page, Like


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city"]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["page_name"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["likes"]
