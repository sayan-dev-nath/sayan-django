from django.shortcuts import render, redirect
from .forms import Registration
from .models import Profile


# Create your views here.
def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            Profile.objects.create(name=name, email=email, password=password).save()
            return redirect("register")
    else:
        form = Registration()
    return render(request, "student/register.html", {"form": form})
