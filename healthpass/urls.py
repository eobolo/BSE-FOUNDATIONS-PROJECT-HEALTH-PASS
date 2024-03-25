from django.urls import path
from . import views
from . import views2
from . import views3

app_name = "healthpass"
urlpatterns = [
    path("user_signup/", views2.UserSignUp.as_view(), name="user_signup"),
    path("user_home/", views2.UserHome.as_view(), name="user_home"),
    path("custom_signup/", views.CustomSignUp.as_view(), name="custom_signup"),
    path("custom_login/", views.CustomLogin.as_view(template_name="healthpass/custom_login.html"), name="custom_login"),
    path("custom_home/", views.CustomHome.as_view(), name="custom_home"),
    path("custom_logout/", views.CustomLogout.as_view(), name="custom_logout"),
    # blood work path
    path("blood_work_create/", views3.BloodWorkCreateView.as_view(), name="blood_work_create"),
    path("blood_work_read/", views3.BloodWorkListView.as_view(), name="blood_work_read"),
]
