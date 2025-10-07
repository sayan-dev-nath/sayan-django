from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def home(request):
    context = {"page": "Home"}
    return render(request, "home.html", context)


def about(request):
    context = {"page": "About"}
    return render(request, "about.html", context)


def form(request):
    context = {"page": "Form"}  # always define default context

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        select = request.POST.get("select")

        # You can show submitted data on the same page
        context.update({"name": name, "email": email, "select": select})
        # return redirect("/form/")
    return render(request, "form.html", context)


def djangoform(request):
    if request.method == "POST":
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data["file"]
            # with open("./firstapp/upload/" + file.name, "wb+") as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()

    return render(request, "djangoform.html", {"form": form})


def studentForm(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentForm()

    return render(request, "djangoform.html", {"form": form})


def passwordValidation(request):
    if request.method == "POST":
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()

    return render(request, "djangoform.html", {"form": form})
