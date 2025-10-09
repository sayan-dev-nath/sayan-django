from django.urls import path
from .views import *

urlpatterns = [
    path("add_profile/", add_profile, name="add_profile"),
]
