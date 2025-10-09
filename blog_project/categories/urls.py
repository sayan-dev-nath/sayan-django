from django.urls import path
from .views import *

urlpatterns = [
    path("add_category/", add_category, name="add_category"),
]
