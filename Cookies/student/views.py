from django.shortcuts import render
from datetime import datetime, timedelta, timezone


def setcookie(request):
    response = render(request, "student/setcookie.html")
    # response.set_cookie("token", "t123456")
    # response.set_cookie("token", "t123456", max_age=3600)
    response.set_cookie(
        "token", "t123456", expires=datetime.now(timezone.utc) + timedelta(days=2)
    )
    return response


def getcookie(request):
    # token = request.COOKIES["token"]
    # token = request.COOKIES.get("token")  # when cookie was deleted return none
    token = request.COOKIES.get("token", "'default token'")
    return render(request, "student/getcookie.html", {"token": token})


def delcookie(request):
    response = render(request, "student/delcookie.html")
    response.delete_cookie("token")
    return response


def setsignedcookie(request):
    response = render(request, "student/setsignedcookie.html")
    response.set_signed_cookie("token", "t123456", salt="tk")
    return response


def getsignedcookie(request):
    # token = request.get_signed_cookie("token", salt="tk")
    token = request.get_signed_cookie("token", default="default_token", salt="tk")
    return render(request, "student/getsignedcookie.html", {"token": token})
