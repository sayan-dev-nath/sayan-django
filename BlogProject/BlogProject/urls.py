from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include("authors.urls")),
    path("category/", include("categories.urls")),
    path("", include("home.urls")),
    path("post/", include("posts.urls")),
]
