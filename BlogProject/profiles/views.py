from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages


# Create your views here.
def add_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, f"{form.profile_name} add successfully.")
            return redirect("add_profile")
    else:
        form = ProfileForm()
    return render(request, "add_profile.html", {"form": form})
