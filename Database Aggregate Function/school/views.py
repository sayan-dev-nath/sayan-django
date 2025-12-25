from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count


def home(request):
    student_data = Student.objects.all()

    average = student_data.aggregate(Avg("marks"))
    print(average)

    average = student_data.aggregate(Sum("marks"))
    print(average)

    average = student_data.aggregate(Min("marks"))
    print(average)

    average = student_data.aggregate(Max("marks"))
    print(average)

    average = student_data.aggregate(Count("marks"))
    print(average)

    context = {"students": student_data}
    return render(request, "school/home.html", context)
