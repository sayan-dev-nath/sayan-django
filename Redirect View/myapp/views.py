from django.shortcuts import render
from django.views.generic import RedirectView


class HomeRedirectView(RedirectView):
    url = "https://www.google.com/"
