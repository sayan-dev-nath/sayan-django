from django.urls import path
from .views import home, signuppage, profile, loginpage, user_logout

urlpatterns = [
    path("", home, name="home"),
    path("signuppage/", signuppage, name="signuppage"),
    path("profile/", profile, name="profile"),
    path("loginpage/", loginpage, name="loginpage"),
    path("user_logout/", user_logout, name="user_logout"),
]
