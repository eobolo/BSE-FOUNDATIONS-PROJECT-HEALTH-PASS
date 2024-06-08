from django.shortcuts import render, redirect
from .models import Student, Grade
from .forms_2 import ParentViewForm
from django.urls import reverse
from django.utils.http import urlencode
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import plotly.graph_objs as go
import plotly.io as pio


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


def get_performance_context_bar_charts(grades, current_year):
    all_html_graphs = []
    semester_averages = []
    semester_names = []
    yearly_averages = []
    yearly_name = []
    context_variable = {}

    for grade in grades:
        subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Geography", "Civics", "Agricultural Science", "Economics", "Commerce", "Government", "Nutrition", "Religious Studies", "Technical Drawing", "Literature in English", "Accounting", "Marketing"]
        scores = [
            grade.math_score.score,
            grade.english_score.score,
            grade.physics_score.score,
            grade.chemistry_score.score,
            grade.biology_score.score,
            grade.geography_score.score,
            grade.civics_score.score,
            grade.agricultural_science_score.score,
            grade.economics_score.score,
            grade.commerce_score.score,
            grade.government_score.score,
            grade.nutrition_score.score,
            grade.religious_studies_score.score,
            grade.technical_drawing_score.score,
            grade.literature_in_english_score.score,
            grade.accounting_score.score,
            grade.marketing_score.score
        ]
        fig = go.Figure(data=[go.Bar(x=subjects, y=scores)])
        fig.update_layout(height=600, width=1500, xaxis_title='Subjects', yaxis_title='Scores', title={'text': "Performance report bar chart for each subject", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        chart = pio.to_html(fig, full_html=False)
        all_html_graphs.append(chart)
        semester_averages.append(sum(scores)/len(scores))

    for i in range(0, len(semester_averages)):
        semester_names.append(f"semester-{i+1}")

    fig = go.Figure(data=[go.Bar(x=semester_names, y=semester_averages)])
    fig.update_layout(height=600, width=1500, xaxis_title='Semester', yaxis_title='Semester Averages %', title={'text': "Performance report bar chart per semester", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
    chart = pio.to_html(fig, full_html=False)
    all_html_graphs.append(chart)

    if len(grades.all()) == 3:
        yearly_averages.append(sum(semester_averages)/len(semester_averages))
        yearly_name.append(f"{current_year}")
        fig = go.Figure(data=[go.Bar(x=yearly_name, y=yearly_averages)])
        fig.update_layout(height=600, width=1500, xaxis_title='Year', yaxis_title='Yearly Average %', title={'text': "Performance report bar chart per year", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        chart = pio.to_html(fig, full_html=False)
        all_html_graphs.append(chart)

    context_variable["all_html_graphs"] = all_html_graphs
    print(len(context_variable["all_html_graphs"]))
    return context_variable


def ParentReportSuccess(request):
    template_name = "academic_feedback_sys/parent_report_success.html"
    return render(request, template_name)

def ParentReport(request, password):
    success_template_name = "academic_feedback_sys/parent_report.html"
    error_template_name = "academic_feedback_sys/no_report_view_permission.html"
    link_uuid_password = password

    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        redirect_login_response = set_view_cookies()
        return redirect_login_response
    
    if request.session.get(f"{link_uuid_password}", None):
        # get selected student  and also get the current
        # year, then use this to filter student grade
        # based on current year
        selected_student = Student.objects.filter(
            secret_password="{0}".format(password),
        ).first()
        current_date = datetime.datetime.now()
        current_year = current_date.year
        selected_student_grade  = Grade.objects.filter(
            student=selected_student,
            semester_year__year=current_year,
        ).order_by("semester")
        # check length of selected student grade
        if len(selected_student_grade) == 0:
            context_variable = {}
            context_variable["no_data"] = "No performance report is found yet for {0} {1} {2}".format(
                selected_student.first_name,
                selected_student.middle_name,
                selected_student.last_name
            )
            return render(request, success_template_name, context_variable)
        context_variable = get_performance_context_bar_charts(selected_student_grade, current_year)
        context_variable["selected_student"] = selected_student
        return render(request, success_template_name, context_variable)
    # return error template
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




