from django.urls import path
from .views import add_profile

urlpatterns = [
    path("add_profile/", add_profile, name="add_profile"),
]
