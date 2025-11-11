from django import forms

# from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class AuthorForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({"class": "form-control"})

#     class Meta:
#         model = Author
#         fields = "__all__"


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "requried"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "requried"}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class ChangeUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
