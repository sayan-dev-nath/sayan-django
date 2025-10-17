from django.shortcuts import render
from .models import *


# Create your views here.
def all_data(request):
    students = Profile.objects.all()
    return render(request, "student/all_data.html", {"students": students})


def single_data(request):
    student = Profile.objects.get(pk=0)
    return render(request, "student/single_data.html", {"student": student})
