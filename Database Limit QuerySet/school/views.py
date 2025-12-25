from django.shortcuts import render
from .models import Student
from django.db.models import Q


def home(request):
    # student_date = Student.objects.all()

    # student_date = Student.objects.all()[:2]

    # student_date = Student.objects.all()[3:5]

    student_date = Student.objects.all()[:5:2]

    context = {"students": student_date}
    return render(request, "school/home.html", context)
