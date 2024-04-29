from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def index_view(request):
    return render(request, "student/index.html")


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def attendance_view(request):
    return render(request, "student/attendance.html")
