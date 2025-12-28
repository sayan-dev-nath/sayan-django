from django.urls import path
from .views import StudentDeleteView
from django.views.generic import TemplateView

urlpatterns = [
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="delete"),
    path(
        "thank/", TemplateView.as_view(template_name="myapp/thank.html"), name="thank"
    ),
]
