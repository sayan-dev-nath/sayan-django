from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def add_post(request):
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect("add_post")
    else:
        post = PostForm()
    context = {"page": "Post", "form": post}
    return render(request, "add_post.html", context)


def delete_post(request, id):
    Post.objects.get(id=id).delete()
    return redirect("/")


def edit_post(request, id):
    post = Post.objects.get(id=id)
    postform = PostForm(instance=post)
    if request.method == "POST":
        postform = PostForm(request.POST, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect("/")
    # else:
    #     post = PostForm()
    context = {"page": "Post", "form": postform}
    return render(request, "add_post.html", context)
