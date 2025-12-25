from django.shortcuts import render
from student.models import Student, Teacher


def home(request):
    data = Student.objects.all()
    return render(request, "student/home.html", {"data": data})
