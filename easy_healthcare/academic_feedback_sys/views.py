from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.http import urlencode
# Create your views here.

# global utility variables
cookie_time = 60 * 60 * 3

# global utility functions
def set_view_cookies(view_request):
    login_url = reverse('login') + '?' + urlencode({"next": view_request.path})
    redirect_login_response = redirect(login_url)
    redirect_login_response.set_cookie("session-cookie", "short-cookie")
    redirect_login_response.set_cookie("timed-cookie", "long-cookie", max_age=cookie_time)
    return redirect_login_response


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
    # if the user isn't a staff send the person to a warning page
    # TODO later, but for now just pass
    pass

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
    pass

@login_required
def TeacherRecentGraded(request):
    pass