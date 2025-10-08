from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User


def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect("/recipes/")
    recipes = Recipe.objects.all()

    if request.GET.get("search_recipe"):
        recipes = recipes.filter(
            recipe_name__icontains=request.GET.get("search_recipe")
        )

    return render(
        request, "recipes.html", context={"page": "Add Recipe", "recipes": recipes}
    )


def update_recipe(request, id):
    quaryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        quaryset.recipe_name = recipe_name
        quaryset.recipe_description = recipe_description

        if recipe_image:
            quaryset.recipe_image = recipe_image

        quaryset.save()
        return redirect("/recipes/")
    context = {"recipe": quaryset, "page": "Update Recipe"}
    return render(request, "update_recipe.html", context)


def delete_recipe(request, id):
    quaryset = Recipe.objects.get(id=id)
    quaryset.delete()
    return redirect("/recipes/")


def login(request):
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            return redirect("/register/")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect("/register/")
    return render(request, "register.html")
