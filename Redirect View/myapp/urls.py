from django.urls import path
from django.views.generic import RedirectView, TemplateView
from .views import *

urlpatterns = [
    path("", TemplateView.as_view(template_name="myapp/home.html"), name="home"),
    # path("home/", RedirectView.as_view(url="/"), name="home1"),
    path("home/", HomeRedirectView.as_view(), name="home1"),
]
