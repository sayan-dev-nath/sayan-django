from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Student


# Default Template
# class StudentDeleteView(DeleteView):
#     model = Student
#     success_url = "/thank/"
#     # fileName = modelName_confirm_delete.html


# Custom Template
class StudentDeleteView(DeleteView):
    model = Student
    success_url = "/thank/"
    template_name = "myapp/delete.html"
