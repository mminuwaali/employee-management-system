from . import models, forms
from django.db.models import Avg
from django.contrib import messages
from employee.models import ClassRoom
from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from account.forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def index_view(request):
    rooms = ClassRoom.objects.filter(students__user=request.user)
    attendances = models.Attendance.objects.filter(student__user=request.user)
    attendance_today = models.Attendance.objects.filter(
        student__user=request.user, check_in__date=datetime.today()
    ).first()

    performance = (
        attendances.aggregate(Avg("status", default=0))["status__avg"] * 100
        if attendances
        else 0
    )

    if request.method == "POST":
        if attendance_today:
            attendance_today.save()
        else:
            models.Attendance.objects.create(student=request.user.student)

        messages.success(request, "Attendance marked successfully")
        return redirect("student:index-view")

    context = {
        "rooms": rooms,
        "attendances": attendances,
        "performance": performance,
        "attendance_today": attendance_today,
    }
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


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def room_detail_view(request, id):
    room = ClassRoom.objects.get(id=id)
    assessments = models.AssessmentAnswer.objects.filter(
        student=request.user.student, assessment__classroom=room
    )

    if request.method == "POST":
        ass_id = request.POST.get("assessment")
        answer = request.POST.get("answer")

        assessment = assessments.get(id=ass_id)
        assessment.answer = answer or assessment.answer
        assessment.save()

        messages.success(request, "Answer has been setup")
        return redirect("student:room-view", id=id)

    context = {"room": room, "assessments": assessments}
    return render(request, "student/room/detail.html", context)
