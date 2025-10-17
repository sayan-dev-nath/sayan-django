from django.urls import path
from .views import *

urlpatterns = [
    path("generate/", generate_qr, name="generate_qr"),
    path("scan/", scan_qr, name="scan_qr"),
]
