from django.urls import path
from . import views


app_name = "academic_feedback_sys"

urlpatterns = [
    path("teacherhome/", views.TeacherHome, name="staff"),
]
