from django.shortcuts import render
from django.views import View
from .models import Student
from django.views.generic import ListView


class AllStudentView(View):
    def get(self, request):
        all_student = Student.objects.all()
        return render(request, "myapp/all_student.html", {"all_student": all_student})


class StudentListView(ListView):
    model = Student
    # file_name = modelName_list.html
    # context_name = modelName_list (default)


class StudentListView1(ListView):
    model = Student
    template_name = "myapp/all_student.html"
    context_object_name = "all_student"
    ordering = ["name"]
    # template_name_suffix = "_all"

    def get_queryset(self):
        return Student.objects.filter(course="python")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["freshers"] = Student.objects.filter(course="economic")
        return context

    def get_template_names(self):
        if self.request.COOKIES.get("user") == "sayan":
            template_name = "myapp/sayan.html"
        else:
            template_name = self.template_name
        return [template_name]
