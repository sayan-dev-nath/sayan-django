from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", SingleStudentView.as_view(), name="single_student"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
]
