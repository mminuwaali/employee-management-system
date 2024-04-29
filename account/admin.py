from . import models
from django.contrib import admin


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ["gender", "marital_status"]
    list_display = ["user", "nationality", "gender", "marital_status"]
