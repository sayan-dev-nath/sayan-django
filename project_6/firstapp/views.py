from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students": students})


def delete_student(request, roll):
    Student.objects.get(roll=roll).delete()
    return redirect("/")


def add_student(request):
    if request.method == "POST":
        data = request.POST
        Student.objects.create(
            name=data.get("name"), roll=data.get("roll"), address=data.get("address")
        )
        return redirect("/")
    return render(request, "add_student.html")


def student_model_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        return redirect("student_model_form")
    else:
        form = StudentForm()
    return render(request, "student_model_form.html", {"form": form})
