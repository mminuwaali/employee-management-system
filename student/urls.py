from . import views
from django.urls import path

app_name, urlpatterns = "student", [
    path("", views.index_view, name="index-view"),
    path("profile/", views.profile_view, name="profile-view"),
    path("attendance/", views.attendance_view, name="attendance-view"),
    path("room/<id>/", views.room_detail_view, name="room-detail-view"),
]
