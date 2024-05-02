from . import views
from django.urls import path

app_name, urlpatterns = "employee", [
    path("", views.index_view, name="index-view"),
    path("room/", views.room_view, name="course-view"),
    path("leave/", views.leave_view, name="leave-view"),
    path("profile/", views.profile_view, name="profile-view"),
    path("assessment/", views.assessment_view, name="assessment-view"),
    path("attendance/", views.attendance_view, name="attendance-view"),
    path("room/<id>/", views.room_detail_view, name="course-detail-view"),
    path("assessment/<id>/", views.assessment_detail_view, name="assessment-detail-view"),
]
