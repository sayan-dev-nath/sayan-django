from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Full Name: ",
        help_text="Total length must be within 70 characters.",
        initial="Rahim Islam",
        required=False,
        # disabled=True,
        # widget=forms.Textarea(
        #     attrs={"id": "text_area", "placeholder": "Enter your full name..."}
        # ),
    )
    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    appointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "datetime-local"})
    )

    CHOICES = [("s", "small"), ("m", "medium"), ("l", "large")]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    MEAL = [("p", "pepperoni"), ("m", "mashroom"), ("b", "beef")]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# validation checking
# class StudentForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Enter your name here..."})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={"placeholder": "Enter your email here..."})
#     )

# def clean_name(self):
#     valname = self.cleaned_data["name"]
#     if len(valname) < 10:
#         raise forms.ValidationError("Enter a name with at least 10 characters")
#     return valname

# def clean_email(self):
#     valemail = self.cleaned_data["email"]
#     if ".com" not in valemail:
#         raise forms.ValidationError("Your email must contain '.com'")
#     return valemail

# def clean(self):
#     valname = self.cleaned_data["name"]
#     valemail = self.cleaned_data["email"]
#     if len(valname) < 10:
#         raise forms.ValidationError("Enter a name with at least 10 characters")
#     if ".com" not in valemail:
#         raise forms.ValidationError("Your email must contain '.com'")


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 characters.")


class StudentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        validators=[
            validators.MinLengthValidator(
                10, message="Enter a name with at least 10 characters"
            )
        ],
    )
    email = forms.EmailField(
        widget=forms.EmailInput,
        validators=[validators.EmailValidator(message="Enter a valid email address")],
    )
    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            validators.MaxValueValidator(34, message="Age cannot be more than 34"),
            validators.MinValueValidator(24, message="Age must be 24 or older"),
        ],
    )
    file = forms.FileField(
        validators=[
            validators.FileExtensionValidator(allowed_extensions=["pdf", "png"])
        ]
    )
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        valpassword = self.cleaned_data["password"]
        valconfirmpassword = self.cleaned_data["confirmPassword"]
        if valpassword != valconfirmpassword:
            raise forms.ValidationError("Password doesn't match.")
