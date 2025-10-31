from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_page")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES["recipe_image"]

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        ).save()
        messages.success(request, "Recipe add successfully")
        return redirect("recipes")
    queryset = Recipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get("search"))

    context = {"recipes": queryset}
    return render(request, "recipes/recipes.html", context)


@login_required(login_url="login_page")
def delete_recipe(request, id):
    Recipe.objects.get(id=id).delete()
    messages.success(request, "Recipe delete successfully")
    return redirect("recipes")


@login_required(login_url="login_page")
def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.recipe_name = request.POST.get("recipe_name")
        recipe.recipe_description = request.POST.get("recipe_description")

        if "recipe_image" in request.FILES:
            recipe.recipe_image = request.FILES["recipe_image"]

        recipe.save()
        messages.success(request, "Recipe update successfully.")
        return redirect("recipes")

    context = {"recipe": recipe}
    return render(request, "recipes/update.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("login_page")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect("login_page")

        login(request, user)
        messages.success(request, "Login successfully")
        return redirect("recipes")

    return render(request, "recipes/login.html")


@login_required(login_url="login_page")
def logout_page(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect("login_page")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "Username already exists")
            return redirect("register")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Registration successfully")
        return redirect("login_page")

    return render(request, "recipes/register.html")
