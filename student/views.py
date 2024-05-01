from . import models, forms
from django.contrib import messages
from employee.models import ClassRoom
from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from account.forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def index_view(request):
    attendance_today = models.Attendance.objects.filter(
        student__user=request.user, check_in__date=datetime.today()
    ).first()

    print(request.user.student.classroom.all())

    if request.method == "POST":
        if attendance_today:
            attendance_today.save()
        else:
            models.Attendance.objects.create(student=request.user.student)

        messages.success(request, "Attendance marked successfully")
        return redirect("student:index-view")

    context = {"attendance_today": attendance_today}
    return render(request, "student/index.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def attendance_view(request):
    if request.method == "POST":
        form = forms.AttendanceForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Attendance recorded successfully")
        else:
            [messages.error(request, i[0]) for i in form.errors.values()]
        return redirect("student:attendance-view")

    attendances = models.Attendance.objects.filter(student__user=request.user)
    context = {"attendances": attendances}
    return render(request, "student/attendance.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
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

            return redirect("student:profile-view")

    return render(request, "student/profile.html")
