from django.urls import path
from .views import ContactFormView, StudentFormView
from django.views.generic import TemplateView


urlpatterns = [
    path("", ContactFormView.as_view(), name="contact"),
    path("register/", StudentFormView.as_view(), name="register"),
    path(
        "thank/",
        TemplateView.as_view(template_name="myapp/thankyou.html"),
        name="thank",
    ),
]
