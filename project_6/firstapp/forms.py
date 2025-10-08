from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = "__all__"
        fields = ["name", "roll", "father_name"]
        # exclude = ["address"]
        labels = {
            "name": "Student Name",
            "roll": "Student Roll",
            "father_name": "Father Name",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your name"}),
            "roll": forms.NumberInput(attrs={"placeholder": "Enter your roll"}),
        }
        help_texts = {
            "name": "write your full name.",
        }
        error_messages = {
            "name": {"required": "Your name is required"},
        }
