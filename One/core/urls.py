from django.contrib import admin
from django.urls import path
from home.views import home, success_page, about, contact
from vege.views import (
    recipes,
    delete_recipe,
    update_recipe,
    login_page,
    register,
    logout_page,
)

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("success_page/", success_page, name="success_page"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("recipes/", recipes, name="recipes"),
    path("delete_recipe/<id>/", delete_recipe, name="delete_recipe"),
    path("update_recipe/<id>/", update_recipe, name="update_recipe"),
    path("login_page/", login_page, name="login_page"),
    path("register/", register, name="register"),
    path("logout_page/", logout_page, name="logout_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
