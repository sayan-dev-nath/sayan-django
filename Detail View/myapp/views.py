from django.shortcuts import render
from django.views import View
from .models import Student
from django.views.generic import DetailView


class SingleStudentView(View):
    def get(self, request, pk):
        single_student = Student.objects.get(pk=pk)
        return render(
            request, "myapp/single_student.html", {"single_student": single_student}
        )


class StudentDetailView(DetailView):
    model = Student
    # default
    # fileName = model_detail.html
    # context = modelName(smallLetter)
    # pk_url_kwarg = "geek"
    # template_name_suffix = "_jankari"
    # template_name = "myapp/single_student.html"
    # context_object_name = "stu"

    # context add korte caile, function ta call korte hbe
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all().order_by("name")
        return context
