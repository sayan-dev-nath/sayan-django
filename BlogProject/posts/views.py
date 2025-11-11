from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.post_author = request.user
            form.save()
            messages.success(request, "Post added successfully.")
            return redirect("add_post")
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form": form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("home")


@login_required
def edit_post(request, id):
    data = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.instance.post_author = request.user
            form.save()
            messages.success(request, "Post edited successfully")
            return redirect("home")
    else:
        form = PostForm(instance=data)
    return render(request, "add_post.html", {"form": form})
