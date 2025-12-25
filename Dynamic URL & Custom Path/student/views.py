from django.shortcuts import render


def home(request):
    return render(request, "student/home.html")


# def profile(request, id):
#     id = {"id": id}
#     return render(request, "student/profile.html", id)


def profile(request, year):
    year = {"year": year}
    return render(request, "student/profile.html", year)
