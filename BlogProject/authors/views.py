from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from posts.models import Post

# from .forms import AuthorForm
# Create your views here.
# def add_author(request):
#     if request.method == "POST":
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form = form.save()
#             messages.success(request, f"{form.author_name} add successfully.")
#             return redirect("add_author")
#     else:
#         form = AuthorForm()
#     return render(request, "add_author.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, f"{form.first_name} add successfully.")
            return redirect("register")
    else:
        form = RegistrationForm()
    return render(request, "add_author.html", {"form": form, "type": "Registration"})


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successfully")
                return redirect("profile")
            else:
                return redirect("register")
    else:
        form = AuthenticationForm()
    return render(request, "add_author.html", {"form": form, "type": "Login"})


@login_required
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required
def profile(request):
    data = Post.objects.filter(post_author=request.user)
    return render(request, "profile.html", {"data": data})


@login_required
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated successfully.")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "add_author.html", {"form": form, "type": "Password"})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ChangeUserForm(instance=request.user)
    return render(request, "add_author.html", {"form": form, "type": "Profile"})
