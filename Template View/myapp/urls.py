from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("home/", TemplateView.as_view(template_name="myapp/home.html"), name="home"),
    path("about/", AboutTemplateView.as_view(), name="about"),
]
