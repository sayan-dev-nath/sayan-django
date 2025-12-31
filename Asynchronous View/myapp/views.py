from django.shortcuts import render, HttpResponse


# synchronous view
def home(request):
    return HttpResponse("<h1>Hello Home Page</h1>")


# asynchronous view
async def home(request):
    return HttpResponse("<h1>Hello Home Page</h1>")
