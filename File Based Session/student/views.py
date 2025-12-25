from django.shortcuts import render


def setsession(request):
    request.session["fastname"] = "Sonam"
    request.session["lastname"] = "Kumari"
    return render(request, "student/setsession.html")


def getsession(request):
    fastname = request.session.get("fastname")
    lastname = request.session.get("lastname")
    return render(
        request, "student/getsession.html", {"fastname": fastname, "lastname": lastname}
    )


def sessionclear(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, "student/sessionclear")
