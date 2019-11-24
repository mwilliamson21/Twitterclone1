from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
