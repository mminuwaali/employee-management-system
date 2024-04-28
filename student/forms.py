from . import models
from django import forms


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = models.Enrollment
        fields = ["email", "username", "last_name", "first_name"]
