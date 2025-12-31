from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm, StudentForm
from .models import Student
from django.contrib import messages


class ContactFormView(FormView):
    template_name = "myapp/contact.html"
    form_class = ContactForm
    success_url = "/thank/"
    initial = {"name": "Sayan", "email": "sayan@example.com"}

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Thare was an error with your form submission.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = True
        return context


class StudentFormView(FormView):
    template_name = "myapp/register.html"
    form_class = StudentForm
    success_url = "/thank/"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        roll = form.cleaned_data["roll"]
        course = form.cleaned_data["course"]
        Student.objects.create(name=name, roll=roll, course=course).save()
        return super().form_valid(form)
