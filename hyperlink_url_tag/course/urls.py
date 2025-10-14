from django.urls import path
from .views import *

urlpatterns = [
    path("django/", learn_django, name="django"),
    path("python/", learn_python, name="python"),
]
