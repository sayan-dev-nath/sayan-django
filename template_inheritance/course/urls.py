from django.urls import path
from .views import *

urlpatterns = [
    path("django/", learn_django, name="learn_django"),
    path("python/", learn_python, name="learn_python"),
]
