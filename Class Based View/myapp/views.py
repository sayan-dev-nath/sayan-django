from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views import View


# def myfunview1(request):
#     return HttpResponse("Hello Function Based View")


class MyClassView1(View):
    def get(self, request):
        return HttpResponse("Hello Class Based View1")


# def myfunview2(request):
#     return HttpResponse("<h1>Function Based View</h1>")


class MyClassView2(View):
    def get(self, request):
        return HttpResponse("<h1>Class Based View2</h1>")


# def homefunview(request):
#     return render(request, "myapp/home.html")


class HomeClassView(View):
    def get(self, request):
        return render(request, "myapp/home.html")


# def aboutfunview(request):
#     context = {"msg": "Welcome to GeekyShows Function Based View"}
#     return render(request, "myapp/about.html", context)


class AboutClassView(View):
    def get(self, request):
        context = {"msg": "Welcome to GeekyShows Class Based View"}
        return render(request, "myapp/about.html", context)


def newsfunview(request):
    context = {"info": "Subscribe to Geekyshows YT Channel"}
    return render(request, "myapp/news.html", context)


# def news2funview(request, template_name):
#     context = {"info": "Subscribe to Geekyshows YT Channel"}
#     return render(request, template_name, context)


class NewsClassView(View):
    template_name = ""

    def get(self, request):
        context = {"info": "Subscribe to Geekyshows YT Channel"}
        return render(request, self.template_name, context)


# def contactfunview(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data["name"])
#             return HttpResponse("Thank You Form Submitted !!")
#     else:
#         form = ContactForm()
#     return render(request, "myapp/contact.html", {"form": form})


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "myapp/contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            return HttpResponse("Thank You Form Submitted !!")
