from django.shortcuts import render


def show_meals(request):
    return render(request, "meals/index.html")
