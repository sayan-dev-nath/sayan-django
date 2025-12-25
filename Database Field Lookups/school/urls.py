from django.urls import path
from school.views import home

urlpatterns = [
    path("", home, name="home"),
]
