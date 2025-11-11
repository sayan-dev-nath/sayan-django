from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Category
        fields = "__all__"
