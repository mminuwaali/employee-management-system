from decimal import Decimal
from . import forms, models
from django.db.models import Avg
from django.contrib import messages
from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from account.forms import ProfileForm, UserForm
from student.models import Student, AssessmentAnswer
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def index_view(request):
    attendances = models.Attendance.objects.filter(employee__user=request.user)
    leaves = models.Leave.objects.filter(employee__user=request.user, status=True)

    attendance_today = attendances.filter(check_in__date=datetime.today()).first()
    performance = attendances.aggregate(Avg("status",default=0))["status__avg"] * 100 if attendances else 0

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
        "performance": performance,
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


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def room_view(request):
    rooms = models.ClassRoom.objects.filter(employee__user=request.user)

    context = {"rooms": rooms}
    return render(request, "employee/course/index.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def room_detail_view(request, id):
    room = models.ClassRoom.objects.get(id=id)

    context = {"room": room}
    return render(request, "employee/course/detail.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def assessment_view(request):
    rooms = models.ClassRoom.objects.filter(employee__user=request.user)
    students = Student.objects.filter(classroom__in=rooms).distinct()
    assessments = models.Assessment.objects.filter(
        classroom__employee__user=request.user
    )

    if request.method == "POST":
        room = request.POST.get("room")
        question = request.POST.get("question")
        students_ids = request.POST.getlist("students")

        assessment, _ = models.Assessment.objects.get_or_create(
            question=question, classroom=rooms.get(id=room)
        )

        for id in students_ids:
            student = students.get(id=id)
            AssessmentAnswer.objects.get_or_create(
                student=student, assessment=assessment
            )

        return redirect("employee:assessment-view")

    context = {"assessments": assessments, "students": students, "rooms": rooms}
    return render(request, "employee/assessment/index.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="employee").exists())
def assessment_detail_view(request, id):
    assessment = models.Assessment.objects.get(id=id)
    answers = AssessmentAnswer.objects.filter(assessment=assessment)
    classroom_students = Student.objects.filter(classroom=assessment.classroom)
    
    unassigned_students = classroom_students.exclude(
        id__in=assessment.classroom.students.all()
    )

    if request.method == "POST":
        type = request.POST.get("type")

        if type == "assign":
            ids = request.POST.getlist("students")
            for id in ids:
                try:
                    student = unassigned_students.get(id=id)
                    AssessmentAnswer.objects.get_or_create(
                        student=student, assessment=assessment
                    )
                except:
                    ...

        elif type == "grade":
            score = request.POST.get("score", 0)
            student = request.POST.get("student")

            try:
                answer = answers.get(student__id=student)
                answer.score = Decimal(score)
                answer.save()
            except:
                ...

        return redirect("employee:assessment-detail-view", id=id)

    context = {
        "answers": answers,
        "assessment": assessment,
        "unassigned_students": unassigned_students,
    }
    return render(request, "employee/assessment/detail.html", context)
