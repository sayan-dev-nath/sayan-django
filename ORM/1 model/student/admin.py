from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Result)


# Model Admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "roll", "email", "city")


admin.site.register(Profile, ProfileAdmin)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("cls", "marks")
