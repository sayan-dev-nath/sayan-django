from django.shortcuts import render
from .models import Page, Post, Song
from django.contrib.auth.models import User


def home(request):
    return render(request, "myapp/home.html")


def show_page_data(request):
    return render(request, "myapp/page.html")


def show_post_data(request):
    return render(request, "myapp/post.html")


def show_song_data(request):
    return render(request, "myapp/song.html")


def show_user_data(request):
    data = User.objects.all()
    data2 = User.objects.filter(page__category="Tech")  # modelName__category="Tech"
    data3 = User.objects.filter(post__publish="2025-12-25")
    return render(
        request,
        "myapp/user.html",
        {"data": data, "data2": data2, "data3": data3},
    )
