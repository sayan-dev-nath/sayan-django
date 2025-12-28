from django.shortcuts import render
from django.views import View
from .models import Student


class AllStudentView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "myapp/students.html", {"students": students})
