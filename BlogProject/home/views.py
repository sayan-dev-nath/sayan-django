from django.shortcuts import render
from posts.models import Post
from categories.models import Category


# Create your views here.
def home(request, category_slug=None):
    post_data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(category_slug=category_slug)
        post_data = Post.objects.filter(post_category=category)
    category_data = Category.objects.all()
    return render(request, "home.html", {"data": post_data, "category": category_data})
