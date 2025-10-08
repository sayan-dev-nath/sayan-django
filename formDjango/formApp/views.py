from django.shortcuts import render
from formApp.forms import contactForm


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


def djangoForm(request):
    # form = contactForm(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    # return render(request, "django_form.html", {"form": form})
    if request.method == "POST":
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            with open("./formApp/upload/" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, "django_form.html", {"form": form})
    else:
        form = contactForm()
        return render(request, "django_form.html", {"form": form})
