from django.shortcuts import render, redirect
from .models import Student, Grade
from .forms_2 import ParentViewForm
from django.urls import reverse
from django.utils.http import urlencode
from . import views
import datetime


# global utility variables
# cookie_time = 60 * 60 * 3

# def set_view_cookies(view_request):
#     login_url = reverse('') + '?' + urlencode({"next": view_request.path})
#     redirect_login_response = redirect(login_url)
#     redirect_login_response.set_cookie("session-cookie", "short-cookie")
#     redirect_login_response.set_cookie("timed-cookie", "long-cookie", max_age=cookie_time)
#     return redirect_login_response


def ParentLoginPlatform(request):
    template_name = "academic_feedback_sys/parent_login.html"
    context_variable = {}
    if request.method == "GET":
        parent_form = ParentViewForm()
        context_variable["parent_form"] = parent_form
        return render(request, template_name, context_variable)
    
    # if the request method is not get check if it is post
    if request.method == "POST":
        # get the POST data and extract the field value
        # then checkk if the student with that values exist
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")

        # check if student exists
        check_if_student_exists = Student.objects.filter(
            first_name=first_name.capitalize(),
            middle_name=middle_name.capitalize(),
            last_name=last_name.capitalize(),
            secret_password=password
        )