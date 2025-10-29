from django.shortcuts import render, redirect
from .models import Food
from .forms import MealAddForm


def show_meals(request):
    foods = Food.objects.all()
    return render(request, "meals/index.html", {"foods": foods})


def add_meal(request):
    if request.method == "POST":
        form = MealAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("add_meal")
    else:
        form = MealAddForm()
    return render(request, "meals/add_meal.html", {"form": form})
