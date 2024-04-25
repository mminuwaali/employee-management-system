from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm


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
