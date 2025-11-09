from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, Post
from django.contrib import messages


# Create your views here.
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, f"{form.post_title} add successfully.")
            return redirect("add_post")
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form": form})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("home")


def edit_post(request, id):
    data = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited successfully")
            return redirect("home")
    else:
        form = PostForm(instance=data)
    return render(request, "add_post.html", {"form": form})
