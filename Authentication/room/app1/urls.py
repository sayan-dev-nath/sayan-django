from django.urls import path
from .views import (
    home,
    signuppage,
    profile,
    loginpage,
    user_logout,
    password_change,
    password_change1,
)

urlpatterns = [
    path("", home, name="home"),
    path("signuppage/", signuppage, name="signuppage"),
    path("profile/", profile, name="profile"),
    path("loginpage/", loginpage, name="loginpage"),
    path("user_logout/", user_logout, name="user_logout"),
    path("password_change/", password_change, name="password_change"),
    path("password_change1/", password_change1, name="password_change1"),
]
