from django.urls import path
from student.views import home, course, result
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", home, name="home"),
    path("course/", course, name="course"),
    path("result/", cache_page(30)(result), name="result"),
]
