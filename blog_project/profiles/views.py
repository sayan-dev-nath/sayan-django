from django.shortcuts import render, redirect
from .forms import ProfileForm


# Create your views here.
def add_profile(request):
    if request.method == "POST":
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            profile.save()
            return redirect("add_profile")
    else:
        profile = ProfileForm()
    context = {"page": "Profile", "form": profile}
    return render(request, "add_profile.html", context)
