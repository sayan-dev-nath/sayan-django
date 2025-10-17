from django import forms
from .models import Profile


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["student_name", "email", "password"]
        labels = {
            "student_name": "Full Name",
            "email": "Email",
            "password": "Password",
        }
        error_messages = {
            "student_name": {"required": "Student name is required."},
            "email": {"required": "Email is required."},
            "password": {"required": "Password is required."},
        }
        widgets = {
            "student_name": forms.TextInput(
                attrs={"placeholder": "Enter full name here..."}
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Enter email here..."}),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Enter password here..."}
            ),
        }


class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ["teacher_name", "email", "password"]
        labels = {
            "teacher_name": "Teacher Full Name",
            "email": "Email",
            "password": "Password",
        }
        error_messages = {
            "teacher_name": {"required": "Teacher name is required"},
            "email": {"required": "Email is required."},
            "password": {"required": "Password is required."},
        }
        widgets = {
            "teacher_name": forms.TextInput(
                attrs={"placeholder": "Enter full name here..."}
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Enter email here..."}),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Enter password here..."}
            ),
        }
