from django.urls import path
from .views import *

urlpatterns = [
    path("", AllStudentView.as_view(), name="all_student"),
    path("students/", StudentListView.as_view(), name="students"),
    path("students1/", StudentListView1.as_view(), name="students1"),
]
