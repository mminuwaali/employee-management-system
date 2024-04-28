from . import views
from django.urls import path

app_name, urlpatterns = "student", [
    path("", views.index_view, name="index-view"),
    path("attendance/", views.attendance_view, name="attendance-view"),
]
