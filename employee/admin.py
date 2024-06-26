from . import models
from django.contrib import admin


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ["department", "position"]
    list_display = ["user", "position", "department", "date_joined"]


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ["employee"]
    list_display = ["employee", "check_in", "check_out"]


@admin.register(models.Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_filter = ["employee", "status"]
    list_display = ["employee", "status", "start_date", "end_date"]


@admin.register(models.ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_filter = ["course", "employee"]
    list_display = ["course", "employee"]


@admin.register(models.Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_filter = ["classroom"]
    search_fields = ["question__startswith"]
    list_display = ["question", "classroom", "created_at", "updated_at"]
