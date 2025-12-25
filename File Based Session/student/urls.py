from django.urls import path
from student.views import setsession, getsession, sessionclear

urlpatterns = [
    path("set/", setsession),
    path("get/", getsession),
    path("clear/", sessionclear),
]
