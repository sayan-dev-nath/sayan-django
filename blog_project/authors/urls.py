from django.urls import path
from .views import *

urlpatterns = [
    path("add_author/", add_author, name="add_author"),
]
