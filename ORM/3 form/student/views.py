from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            print("Name:", name)
            print("Email:", email)
            print("Password:", password)
            return redirect("register")
    else:
        form = Registration()
    return render(request, "student/register.html", {"form": form})
