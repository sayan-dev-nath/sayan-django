from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def home(request):
# return HttpResponse("<h1>Hey I am a Django Server.<h1/>")


def home(request):
    peoples = [
        {"name": "sayan", "age": 16},
        {"name": "nayan", "age": 20},
        {"name": "kamal", "age": 20},
    ]
    return render(request, "home/index.html", context={"peoples": peoples})


def success_page(request):
    return HttpResponse("<h1>Hey this is a Success Page.<h1/>")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")
