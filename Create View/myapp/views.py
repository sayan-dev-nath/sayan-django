from django.shortcuts import render
from django.views.generic import CreateView
from .models import Student
from .forms import StudentForm


# class StudentCreateView(CreateView):
# model = Student
# fields = ["name", "email", "password"]

# default
# fileName = modelName_form.html
# success_url = "/https://www.google.com/"

# def get_form(self, form_class=...):
#     return super().get_form(form_class)


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "myapp/student_form.html"
