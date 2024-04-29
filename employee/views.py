from . import forms, models
from django.contrib import messages
from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from account.forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def index_view(request):
    attendances = models.Attendance.objects.filter(employee__user=request.user)
    leaves = models.Leave.objects.filter(employee__user=request.user, status=True)

    attendance_today = attendances.filter(created_at__date=datetime.today()).first()

    if request.method == "POST":
        if attendance_today:
            attendance_today.save()
        else:
            models.Attendance.objects.create(employee=request.user.employee)
        
        messages.success(request, "Attendance marked successfully")
        return redirect("employee:index-view")

    context = {
        "leaves": leaves,
        "attendances": attendances,
        "attendance_today": attendance_today,
    }
    return render(request, "employee/index.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def leave_view(request):
    if request.method == "POST":
        form = forms.LeaveForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Leave recorded successfully")
            return redirect("employee:leave-view")

    leaves = models.Leave.objects.filter(employee__user=request.user)
    context = {"leaves": leaves}
    return render(request, "employee/leave.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def attendance_view(request):
    if request.method == "POST":
        form = forms.AttendanceForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Attendance recorded successfully")
        else:
            [messages.error(request, i[0]) for i in form.errors.values()]
        return redirect("employee:attendance-view")

    attendances = models.Attendance.objects.filter(employee__user=request.user)
    context = {"attendances": attendances}
    return render(request, "employee/attendance.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def profile_view(request):
    form_classes = {"user": UserForm, "profile": ProfileForm}

    if request.method == "POST":
        type = request.POST.get("type")
        form_class = form_classes.get(type)

        if form_class:
            instance = request.user if type == "user" else getattr(request.user, type)
            form = form_class(request.POST, request.FILES, instance=instance)

            if form.is_valid():
                form.save()
                messages.success(request, f"{type.capitalize()} updated successfully")
            else:
                print(form.errors)
                [messages.error(request, error) for error in form.errors.values()]

            return redirect("employee:profile-view")

    return render(request, "employee/profile.html")
