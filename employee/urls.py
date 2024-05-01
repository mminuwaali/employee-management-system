from . import views
from django.urls import path

app_name, urlpatterns = "employee", [
    path("", views.index_view, name="index-view"),
    path("leave/", views.leave_view, name="leave-view"),
    path("course/", views.room_view, name="course-view"),
    path("profile/", views.profile_view, name="profile-view"),
    path("attendance/", views.attendance_view, name="attendance-view"),
    path("course/<id>/", views.room_detail_view, name="course-detail-view"),
]
