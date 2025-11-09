from django.urls import path
from .views import add_post, delete_post, edit_post

urlpatterns = [
    path("add_post/", add_post, name="add_post"),
    path("delete_post/<int:id>/", delete_post, name="delete_post"),
    path("edit_post/<int:id>/", edit_post, name="edit_post"),
]
