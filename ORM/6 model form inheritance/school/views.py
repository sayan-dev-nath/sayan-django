from django.shortcuts import render, redirect
from .forms import StudentRegistration, TeacherRegistration
from .models import Profile


# Create your views here.
def studentreg(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data["student_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            Profile.objects.create(
                student_name=name, email=email, password=password
            ).save()
            return redirect("studentreg")
    else:
        form = StudentRegistration()
    return render(request, "school/studentreg.html", {"form": form})


def teacherreg(request):
    if request.method == "POST":
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data["teacher_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            Profile.objects.create(
                teacher_name=name, email=email, password=password
            ).save()
            return redirect("teacherreg")
    else:
        form = TeacherRegistration()
    return render(request, "school/teacherreg.html", {"form": form})
