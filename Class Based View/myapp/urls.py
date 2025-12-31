from django.urls import path
from .views import *

urlpatterns = [
    # path("fun1/", myfunview1, name="myfunview1"),
    path("fun1/", MyClassView1.as_view(), name="myfunview1"),
    # path("fun2/", myfunview2, name="myfunview2"),
    path("fun2/", MyClassView2.as_view(), name="myfunview2"),
    # path("homefun/", homefunview, name="homefunview"),
    path("homefun/", HomeClassView.as_view(), name="homefunview"),
    # path("aboutfun/", aboutfunview, name="aboutfunview"),
    path("aboutfun/", AboutClassView.as_view(), name="aboutfunview"),
    path("newsfun/", newsfunview, name="newsfunview"),
    # path(
    #     "news2fun/",
    #     news2funview,
    #     {"template_name": "myapp/news2.html"},
    #     name="news2funview",
    # ),
    path(
        "news2fun/",
        NewsClassView.as_view(template_name="myapp/news2.html"),
        name="news2funview",
    ),
    # path("contactfun/", contactfunview, name="contactfunview"),
    path("contactfun/", ContactClassView.as_view(), name="contactfunview"),
]
