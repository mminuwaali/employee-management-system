from . import models
from django.contrib import admin


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["department"]
    list_display = ["user", "date_enrolled", "department"]


@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_filter = ["status"]
    search_fields = ["department", "email", "username"]
    list_display = ["email", "username", "department", "status"]


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ["student"]
    list_display = ["student", "check_in", "check_out"]
