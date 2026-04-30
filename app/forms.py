from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['name','surename','age','picture','phone_number','email']