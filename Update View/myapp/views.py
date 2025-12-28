from django.shortcuts import render
from django.views.generic import UpdateView
from .models import Student
from django import forms

# Default Template
# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ["name", "email", "password"]
#     success_url = "/thank/"


# Custom Template
class StudentUpdateView(UpdateView):
    model = Student
    fields = ["name", "email", "password"]
    success_url = "/thank/"
    template_name = "myapp/register.html"

    def get_form(self):
        form = super().get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "myclass"})
        form.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "mypass"}, render_value=True
        )
        return form
