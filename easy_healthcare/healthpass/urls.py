from django.urls import path
from . import views
from . import views2
from . import views3
from . import views4

app_name = "healthpass"
urlpatterns = [
    # authentication paths
    path("user_signup/", views2.UserSignUp.as_view(), name="user_signup"),
    path("user_home/", views2.UserHome.as_view(), name="user_home"),
    path("custom_signup/", views.CustomSignUp.as_view(), name="custom_signup"),
    path("custom_login/", views.CustomLogin.as_view(template_name="healthpass/custom_login.html"), name="custom_login"),
    path("custom_home/", views.CustomHome.as_view(), name="custom_home"),
    path("custom_logout/", views.CustomLogout.as_view(), name="custom_logout"),
    # blood work paths
    path("blood_work_create/", views3.BloodWorkCreateView.as_view(), name="blood_work_create"),
    path("blood_work_read/", views3.BloodWorkListView.as_view(), name="blood_work_read"),
    path("blood_work_read_update/", views3.BloodWorkUpdateListView.as_view(), name="blood_work_read_update"),
    path("blood_work_update/<int:pk>/", views3.BloodWorkUpdateView.as_view(), name="blood_work_update"),
    path("blood_work_read_delete/", views3.BloodWorkDeleteListView.as_view(), name="blood_work_read_delete"),
    path("blood_work_delete/<int:pk>/", views3.BloodWorkDeleteView.as_view(), name="blood_work_delete"),
    # general info paths
    path("general_info_create/", views3.GeneralInfoCreateView.as_view(), name="general_info_create"),
    path("general_info_read/", views3.GeneralInfoListView.as_view(), name="general_info_read"),
    path("general_info_read_update/", views3.GeneralInfoUpdateListView.as_view(), name="general_info_read_update"),
    path("general_info_update/<int:pk>/", views3.GeneralInfoUpdateView.as_view(), name="general_info_update"),
    path("general_info_read_delete/", views3.GeneralInfoDeleteListView.as_view(), name="general_info_read_delete"),
    path("general_info_delete/<int:pk>/", views3.GeneralInfoDeleteView.as_view(), name="general_info_delete"),
    # urinalysis paths
    path("urinalysis_create/", views3.UrinalysisCreateView.as_view(), name="urinalysis_create"),
    path("urinalysis_read/", views3.UrinalysisListView.as_view(), name="urinalysis_read"),
    path("urinalysis_read_update/", views3.UrinalysisUpdateListView.as_view(), name="urinalysis_read_update"),
    path("urinalysis_update/<int:pk>/", views3.UrinalysisUpdateView.as_view(), name="urinalysis_update"),
    path("urinalysis_read_delete/", views3.UrinalysisDeleteListView.as_view(), name="urinalysis_read_delete"),
    path("urinalysis_delete/<int:pk>/", views3.UrinalysisDeleteView.as_view(), name="urinalysis_delete"),
    # custom blood work read, urinalysis read, and general info read
    path("custom_blood_work_read/", views4.CustomBloodWorkListView.as_view(), name="custom_blood_work_read"),
]
