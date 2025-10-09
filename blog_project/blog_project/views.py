from django.shortcuts import render
from posts.models import Post


def home(request):
    data = Post.objects.all()
    context = {"page": "Home", "data": data}
    return render(request, "home.html", context)
