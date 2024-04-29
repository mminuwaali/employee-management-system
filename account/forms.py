from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ["name", "email", "phone", "message"]


class ProfileForm(forms.ModelForm):
    class Meta:
        exclude = ["user"]
        model = models.Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = [
            "email",
            "username",
            "password1",
            "password2",
            "last_name",
            "first_name",
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["first_name", "last_name"]
