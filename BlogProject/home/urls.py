from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("category/<slug:category_slug>/", home, name="category_wise_post"),
]
