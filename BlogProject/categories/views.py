from django.shortcuts import render, redirect
from .forms import CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, f"{form.category_name} add successfully.")
            return redirect("add_category")
    else:
        form = CategoryForm()
    return render(request, "add_category.html", {"form": form})
