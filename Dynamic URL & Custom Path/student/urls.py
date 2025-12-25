from django.urls import path, register_converter
from student.views import home, profile
from student.converter import FourDigitYearConverter

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", home, name="home"),
    # path("profile/<id>", profile, name="profile"),
    # path("profile/<int:id>", profile, name="profile"),
    # path("profile/<slug:title>", profile, name="profile"),
    path("profile/<yyyy:year>", profile, name="profile"),
]
