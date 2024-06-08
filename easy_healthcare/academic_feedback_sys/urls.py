from django.urls import path
from . import views
from . import views_2


app_name = "academic_feedback_sys"

urlpatterns = [
    # TEACHER PATHS
    path("teacherhome/", views.TeacherHome, name="staff"),
    path("teacherprofile/", views.TeacherProfile, name="profile"),
    path("teacherstudents/", views.TeacherStudents, name="students"),
    path("teacherrecentgraded/", views.TeacherRecentGraded, name="recent_grades"),
    path("teachereditstudent/<str:first_name>/<str:middle_name>/<str:last_name>/", views.TeacherEditStudentGrade, name="edit_student_grade"),
    # PARENT PATHS
    path("parentguardianplatform/", views_2.ParentLoginPlatform, name="parent_login"),
    path("parentguardianreport/<uuid:password>/", views_2.ParentReport, name="report"),
    path("parentguardiansuccess/", views_2.ParentReportSuccess, name="report_success"),
]