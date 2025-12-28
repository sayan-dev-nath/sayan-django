from django.urls import path
from .views import home, contact, product

urlpatterns = [
    path("", home, name="home"),
    path("product/", product, name="product"),
    path("contact/", contact, name="contact"),
]
