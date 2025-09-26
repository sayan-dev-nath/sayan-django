from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    if request.method == "GET":
        name = request.GET.get("name")
        email = request.GET.get("email")
        select = request.GET.get("select")
        return render(
            request, "about.html", {"name": name, "email": email, "select": select}
        )
    else:
        return render(request, "about.html")


def form(request):
    return render(request, "form.html")
