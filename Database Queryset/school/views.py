from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Q


"""def home(request):
    all_data = Student.objects.all()

    print("SQL Query :: ", all_data.query)

    all_data = Student.objects.filter(city="Chittagong")

    all_data = Student.objects.exclude(city="Chittagong")

    all_data = Student.objects.order_by("marks")

    all_data = Student.objects.order_by("-marks")

    all_data = Student.objects.order_by("?")

    all_data = Student.objects.order_by("name")

    all_data = Student.objects.order_by("name").reverse()

    all_data = Student.objects.order_by("name")[0:3]

    all_data = Student.objects.values()
    print(all_data)

    union, intersection, difference, &, |

    all_data = Student.objects.values("id", "name")
    print(all_data)

    return render(request, "school/home.html", {"all_data": all_data})"""


def home(request):
    # data = Student.objects.get(pk=2)

    # data = Student.objects.first()

    # data = Student.objects.last()

    # data = Student.objects.order_by("name").first()

    # data = Student.objects.order_by("name").first()

    # data = Student.objects.latest("pass_date")

    # data = Student.objects.earliest("pass_date")

    data = Student.objects.earliest("pass_date")

    # Student.objects.create(name='Anisa', roll=115, city='Bokaro', marks=60,pass_date='2020-5-4')

    # Student.objects.filter(pk=1).update(name="Kamal")

    # student_data, created = Student.objects.update_or_create(
    #     id=10, name="Anisa", defaults={"name": "Kohli", "roll": 156}
    # )

    return render(request, "school/home.html", {"data": data})
