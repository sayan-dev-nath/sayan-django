from django.shortcuts import render


# Create your views here.
def learn_django(request):
    context = {"page": "Django"}
    return render(request, "course/django.html", context)


def learn_python(request):
    context = {"page": "Python"}
    return render(request, "course/python.html", context)
