from django.shortcuts import render, redirect
from .models import Recipe


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
        return redirect("recipes")

    queryset = Recipe.objects.all()
    context = {"recipes": queryset}

    return render(request, "recipes/recipes.html", context)


def delete_recipe(request, id):
    Recipe.objects.get(id=id).delete()
    return redirect("recipes")


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    context = {"recipe": queryset}
    return render(request, "recipes/recipes.html", context)
