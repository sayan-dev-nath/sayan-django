from django.shortcuts import render
from school.models import Student


def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(name__exact="sayan")

    # student_data = Student.objects.filter(name__iexact="sayan")

    # student_data = Student.objects.filter(name__contains="a")

    # student_data = Student.objects.filter(name__icontains="a")

    # student_data = Student.objects.filter(id__in=[1, 3, 7])

    # student_data = Student.objects.filter(marks__gt=60)

    # student_data = Student.objects.filter(marks__gte=60)

    # student_data = Student.objects.filter(marks__lte=60)

    # student_data = Student.objects.filter(name__startswith="s")

    student_data = Student.objects.filter(name__istartswith="s")

    # print("student_date:", student_data)
    return render(request, "school/home.html", {"student": student_data})
