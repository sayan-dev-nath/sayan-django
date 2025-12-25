from django.shortcuts import render
from django.contrib import messages


def home(request):
    # messages.add_message(request, messages.SUCCESS, "Your account has been created!!!")
    messages.success(request, "This is success!!!")
    return render(request, "student/home.html")


def registration(request):
    return render(request, "student/registration.html")
