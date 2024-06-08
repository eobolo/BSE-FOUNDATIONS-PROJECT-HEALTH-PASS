from django.shortcuts import render, redirect
from .models import Student, Grade
from .forms_2 import ParentViewForm
from django.urls import reverse
from django.utils.http import urlencode
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from . import views
import datetime


# global utility variables
cookie_time = 60 * 60 * 3

def set_view_cookies():
    parent_login = reverse('academic:parent_login')
    redirect_login_response = redirect(parent_login)
    redirect_login_response.set_cookie("session-cookie", "short-cookie")
    redirect_login_response.set_cookie("timed-cookie", "long-cookie", max_age=cookie_time)
    return redirect_login_response

def send_html_email(urllink, email, school_name="child's"):
    subject = "{0} performance report verification email".format(school_name)
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    text_content = "This is an important message."
    html_content = f"""
        <h3>This is an <strong>important</strong> message.</h3>
        <p>
            click on this link if you requested seeing your child's performance <a href='{urllink}'>View report</a>
        </p>
    """
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def ParentReportSuccess(request):
    template_name = "academic_feedback_sys/parent_report_success.html"
    return render(request, template_name)

def ParentReport(request, password):
    success_template_name = "academic_feedback_sys/parent_report.html"
    error_template_name = "academic/no_report_view_permission.html"
    link_uuid_password = password

    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        redirect_login_response = set_view_cookies()
        return redirect_login_response
    
    if request.session.get(f"{link_uuid_password}", None):
        del request.session[f"{link_uuid_password}"]
        return render(request, success_template_name)
    return render(request, error_template_name)

def ParentLoginPlatform(request):
    template_name = "academic_feedback_sys/parent_login.html"
    context_variable = {}
    if request.method == "GET":
        parent_form = ParentViewForm()
        context_variable["parent_form"] = parent_form
        return render(request, template_name, context_variable)
    
    # if the request method is not get check if it is post
    if request.method == "POST":
        # check if form is valid first
        check_parent_form = ParentViewForm(request.POST)
        if not check_parent_form.is_valid():
            context_variable["parent_form"] = check_parent_form
            context_variable["error_message"] = "This form is not valid."
            return render(request, template_name, context_variable)
        
        # get the POST data and extract the field value
        # then checkk if the student with that values exist
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")

        # check if student exists
        get_student = Student.objects.filter(
            first_name=first_name.capitalize(),
            middle_name=middle_name.capitalize(),
            last_name=last_name.capitalize(),
            secret_password=password
        )
        if not get_student.exists():
            parent_form = ParentViewForm(request.POST)
            context_variable["parent_form"] = parent_form
            context_variable["error_message"] = "This user doesn't exist, make sure you put the correct details in the form"
            return render(request, template_name, context_variable)
        
        get_student = get_student.first()
        print(get_student)
        # if user exist we need a confirmation email to send out link where Parent
        # would verify before check the performance reports of their child
        # and also save the uuid for the current session for later verification
        request.session[f"{get_student.secret_password}"] = str(get_student.secret_password)
        url_link = f"https://olugbeminiyi2000.pythonanywhere.com/academic_feedback_sys/parentguardianreport/{password}"
        email = get_student.email
        school_name = "African Leadership University"
        send_html_email(url_link, email, school_name)

        # Now do a PostRedirectGetRequest to a success view telling parent to check email for verification
        return redirect(reverse("academic:report_success"))




