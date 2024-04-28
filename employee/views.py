from . import forms, models
from django.contrib import messages
from django.shortcuts import render, redirect


def index_view(request):
    return render(request, "employee/index.html")


def leave_view(request):
    if request.method == "POST":
        form = forms.LeaveForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Leave recorded successfully")
            return redirect("employee:leave-view")

    return render(request, "employee/leave.html")


def attendance_view(request):
    if request.method == "POST":
        form = forms.AttendanceForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Attendance recorded successfully")
        else:
            [messages.error(request, i[0]) for i in form.errors.values()]
        return redirect("employee:attendance-view")

    return render(request, "employee/attendance.html")
