from django.urls import path
from .views import *

urlpatterns = [
    path("registration/", registration, name="registration"),
    path("login/", login, name="login"),
    path("address/", address, name="address"),
    path("demoform/", demoform, name="demoform"),
]
