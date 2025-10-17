from django import forms
from .models import Profile


class Registration(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # confirm_password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={"placeholder": "Comfirm password"})
    # )

    class Meta:
        model = Profile
        # fields = ["name", "email", "password"]
        fields = "__all__"
        labels = {
            "name": "Name",
            "email": "Email",
        }
        error_messages = {
            "name": {"required": "Name is required"},
            "email": {"required": "Email is required"},
        }
        widgets = {
            "password": forms.PasswordInput(
                attrs={"placeholder": "Enter password here..."}
            ),
            "name": forms.TextInput(attrs={"placeholder": "Enter name here..."}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter email here..."}),
        }


# -----------------------------------------------------------------------------
# class Registration(forms.Form):
#     name = forms.CharField(error_messages={"required": "Name is required"})
#     email = forms.EmailField(error_messages={"required": "Email is required"})
#     password = forms.CharField(
#         widget=forms.PasswordInput,
#         error_messages={"required": "Password is required"},
#     )
