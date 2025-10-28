from django.urls import path
from .views import show_meals

urlpatterns = [
    path("show_meals/", show_meals, name="show_meals"),
]
