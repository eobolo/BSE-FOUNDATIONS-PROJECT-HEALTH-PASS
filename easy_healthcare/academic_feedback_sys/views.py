from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.http import urlencode
from guardian.models import UserObjectPermission
from .models import Student
# Create your views here.

# global utility variables
cookie_time = 60 * 60 * 3
access_denied_error_template = "academic_feedback_sys/no_permission.html"

# global utility functions
def set_view_cookies(view_request):
    login_url = reverse('login') + '?' + urlencode({"next": view_request.path})
    redirect_login_response = redirect(login_url)
    redirect_login_response.set_cookie("session-cookie", "short-cookie")
    redirect_login_response.set_cookie("timed-cookie", "long-cookie", max_age=cookie_time)
    return redirect_login_response

# Custom Error Views
def custom_error_403(request, exception=None):
    return render(request, access_denied_error_template, status=403)

# Teacher Views
@login_required
def TeacherHome(request):
    template_name = "academic_feedback_sys/teacher_home.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        redirect_login_response = set_view_cookies(request)
        return redirect_login_response
    # now check if this user is a staff because some people can create healthpass login
    # and would want to login
    if request.user.is_staff == True:
        # create a context saving the teacher's object
        # can be gotten from request object easily
        # then return a response from the render object
        context_variable = {}
        logged_teacher_obj = request.user
        context_variable["logged_teacher_obj"] = logged_teacher_obj
        return render(request, template_name, context_variable)
    # if the user isn't a staff send the person to a 403 error page
    # TODO later, but for now just pass
    raise PermissionDenied

@login_required
def TeacherProfile(request):
    template_name = "academic_feedback_sys/teacher_profile.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        redirect_login_response = set_view_cookies(request)
        return redirect_login_response
    pass

@login_required
def TeacherStudents(request):
    template_name = "academic_feedback_sys/teacher_students.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        redirect_login_response = set_view_cookies(request)
        return redirect_login_response
    # now check if this user is a staff because some people can create healthpass login
    # and would want to login to this app
    if request.user.is_staff == True:
        # create a context variable to store all students
        # of that class teacher and a id integer list
        # to store the student id's
        id_list = None
        context_variable = {}
        class_teacher = request.user
        # get the class teacher student, based on permission
        # this returns a row of the student(s) that the class
        # teacher as permission to edit their grade
        # but not exactly the students but we have an information
        # we need in those rows i.e the object_pk which is the
        # student primary key i.e id in string
        class_teacher_perm_students = UserObjectPermission.objects.filter(user=class_teacher).all()
        # extract all ids in strings and convert to integers
        # using list comprehension
        id_list = [int(row.object_pk) for row in class_teacher_perm_students]
        # then get all student objects now using this id list
        class_teacher_students = Student.objects.filter(id__in=id_list)
        # now I have all student we can now store it in the context variable
        # and also store class teacher object
        context_variable["class_teacher"] = class_teacher
        context_variable['students'] = class_teacher_students
        return render(request, template_name, context_variable)
    raise PermissionDenied

@login_required
def TeacherRecentGraded(request):
    pass

@login_required
def TeacherEditStudentGrade(request):
    pass