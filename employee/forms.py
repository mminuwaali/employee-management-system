from . import models
from django import forms


class AttendanceForm(forms.ModelForm):
    class Meta:
        fields = ["employee"]
        model = models.Attendance


class LeaveForm(forms.ModelForm):
    class Meta:
        model = models.Leave
        fields = ["employee", "description", "start_date", "end_date"]
