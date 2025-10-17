from django.shortcuts import render
from .forms import *


# Create your views here.
def registration(request):
    form = Registration()
    # form = Registration(field_order=["email", "city"])
    return render(request, "student/registration.html", {"form": form})


def login(request):
    # form = Login(auto_id="sonam_%s")
    # form = Login(auto_id=True)
    # form = Login(auto_id=False)
    # form = Login(auto_id="sonam")

    # form = Login(label_suffix="a")
    # form = Login(label_suffix=" ")

    # form = Login(initial={"email": "sonam@example.com", "password": "12345"})
    # form = Login(
    #     auto_id=True,
    #     label_suffix=" ",
    #     initial={"email": "sonam@example.com", "password": "12345"},
    # )

    form = Login()
    return render(request, "student/login.html", {"form": form})


def address(request):
    form = Address()
    return render(request, "student/address.html", {"form": form})


def demoform(request):
    form = DemoForm()
    return render(request, "student/demoform.html", {"form": form})
