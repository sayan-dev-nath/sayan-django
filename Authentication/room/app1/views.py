from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "home.html")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    else:
        return redirect("loginpage")


def signuppage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully")
                return redirect("signuppage")
        else:
            form = RegisterForm()
        return render(request, "signup.html", {"form": form})
    else:
        return redirect("profile")


def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome, {username}!")
                    return redirect("profile")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    else:
        return redirect("profile")


def user_logout(request):
    logout(request)
    return redirect("loginpage")
