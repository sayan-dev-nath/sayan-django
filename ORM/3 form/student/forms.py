from django import forms
from django.core import validators


# -----------------------Customize Django Form Error Fields----------------------------
class Registration(forms.Form):
    name = forms.CharField(error_messages={"required": "Name is required"})
    eamil = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# -------------------------------------------------------------------------------------
# def start_with_s(value):
#     if value[0] != "s":
#         raise forms.ValidationError("Email should start with 's'")


# class Registration(forms.Form):
#     name = forms.CharField(
#         validators=[
#             validators.MaxLengthValidator(10),
#             validators.MinLengthValidator(3),
#         ]
#     )
#     email = forms.EmailField(validators=[start_with_s])
#     password = forms.CharField(widget=forms.PasswordInput)


# --------------------------------------------------------------------------------------
# class Registration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean_name(self):
#         # self.cleaned_data.get('name')
#         name_value = self.cleaned_data["name"]
#         if len(name_value) < 4:
#             raise forms.ValidationError("Enter more than or equal 4 character")
#         return name_value


#     def clean_email(self):
#         # self.cleaned_data.get('email')
#         email_value = self.cleaned_data["email"]
#         if len(email_value) < 20:
#             raise forms.ValidationError("Enter more than or equal 20 character")
#         return email_value


# --------------------------------------------------------------------------------------
# class Registration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         name_value = cleaned_data.get("name")
#         email_value = cleaned_data.get("email")

#         if name_value and len(name_value) < 4:
#             self.add_error("name", "Enter more than or equal to 4 characters")

#         if email_value and len(email_value) < 20:
#             self.add_error("email", "Enter more than or equal to 20 characters")

#         # print(type(cleaned_data))
#         # print(type(forms.Form))
#         return cleaned_data
