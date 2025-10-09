from django.shortcuts import render, redirect
from .forms import AuthorForm


# Create your views here.
def add_author(request):
    if request.method == "POST":
        authorform = AuthorForm(request.POST)
        if authorform.is_valid():
            authorform.save()
            return redirect("add_author")
    else:
        authorform = AuthorForm()
    context = {"form": authorform, "page": "Author"}
    return render(request, "add_author.html", context)
