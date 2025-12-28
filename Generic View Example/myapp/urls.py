from django.urls import path
from .views import *

urlpatterns = [
    path("create/", StudentCreateView.as_view(), name="create"),
    path("list/", StudentListView.as_view(), name="list"),
    path("detail/<int:pk>/", StudentDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", StudentUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="delete"),
]
