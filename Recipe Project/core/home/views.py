from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html", context={"page": "Home"})


def about(request):
    return render(request, "about.html", context={"page": "About"})


def contact(request):
    return render(request, "contact.html", context={"page": "Contact"})
