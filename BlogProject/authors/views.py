from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.contrib import messages


# Create your views here.
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, f"{form.author_name} add successfully.")
            return redirect("add_author")
    else:
        form = AuthorForm()
    return render(request, "add_author.html", {"form": form})
