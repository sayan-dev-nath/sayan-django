from django import forms
from .models import Student


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll", "course"]
