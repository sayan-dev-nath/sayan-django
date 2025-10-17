from django.urls import path
from .views import studentreg, teacherreg

urlpatterns = [
    path("studentreg/", studentreg, name="studentreg"),
    path("teacherreg/", teacherreg, name="teacherreg"),
]
