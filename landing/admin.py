from . import models
from django.contrib import admin


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    list_display = ["name"]
    search_fields = ["name"]
