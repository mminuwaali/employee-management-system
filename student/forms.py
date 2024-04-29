from . import models
from django import forms

class AttendanceForm(forms.ModelForm):
    class Meta:
        fields = ["student"]
        model = models.Attendance



class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = models.Enrollment
        fields = ["email", "username", "last_name", "first_name"]
