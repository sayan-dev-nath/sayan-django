from django.urls import path

# from .views import add_author
from .views import (
    register,
    login_page,
    logout_page,
    profile,
    password_change,
    edit_profile,
)

urlpatterns = [
    # path("add_author/", add_author, name="add_author"),
    path("register/", register, name="register"),
    path("login_page/", login_page, name="login_page"),
    path("logout_page/", logout_page, name="logout_page"),
    path("profile/", profile, name="profile"),
    path("password_change/", password_change, name="password_change"),
    path("edit_profile/", edit_profile, name="edit_profile"),
]
