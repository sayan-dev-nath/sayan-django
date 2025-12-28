from django.urls import path
from .views import StudentUpdateView
from django.views.generic import TemplateView

urlpatterns = [
    path("update/<int:pk>/", StudentUpdateView.as_view(), name="update"),
    path(
        "thank/",
        TemplateView.as_view(template_name="myapp/thank.html"),
        name="thank",
    ),
]
