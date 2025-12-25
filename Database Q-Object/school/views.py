from django.shortcuts import render
from .models import Student
from django.db.models import Q


def home(request):
    # student_date = Student.objects.all()

    # student_date = Student.objects.filter(Q(id=2) & Q(roll=102))

    # student_date = Student.objects.filter(Q(id=2) | Q(roll=102))

    # student_date = Student.objects.filter(Q(id=3) | Q(roll=102))

    # student_date = Student.objects.filter(~Q(id=3))

    student_date = Student.objects.filter(Q(id=3) | Q(marks__gt=30))

    context = {"students": student_date}
    return render(request, "school/home.html", context)
