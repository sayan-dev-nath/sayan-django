from django.urls import path
from .views import *

urlpatterns = [
    path("dj/", learn_django, name="learn_django"),
]
