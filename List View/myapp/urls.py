from django.urls import path
from .views import AllStudentView

urlpatterns = [
    path("", AllStudentView.as_view(), name="home"),
]
