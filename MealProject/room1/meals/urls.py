from django.urls import path
from .views import show_meals, add_meal

urlpatterns = [
    path("show_meals/", show_meals, name="show_meals"),
    path("add_meal/", add_meal, name="add_meal"),
]
