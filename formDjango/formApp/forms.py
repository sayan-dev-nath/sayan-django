from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField(label="User Age")
    weight = forms.FloatField(label="User Weight")
    balance = forms.DecimalField(label="User Balance")
    check = forms.BooleanField(label="User Check")
    birthday = forms.DateField(label="Birthday")
    appointment = forms.DateTimeField()
    CHOICES = [("s", "small"), ("m", "medium"), ("l", "large")]
    size = forms.ChoiceField(choices=CHOICES)
