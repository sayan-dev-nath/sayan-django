from django.urls import path
from .views import *

urlpatterns = [
    path("all_data/", all_data, name="all_data"),
    path("single_data/", single_data, name="single_data"),
]
