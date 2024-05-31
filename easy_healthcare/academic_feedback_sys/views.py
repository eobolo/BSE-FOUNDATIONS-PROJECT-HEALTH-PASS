from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.http import urlencode
# Create your views here.

# global utility variables
cookie_time = 60 * 60 * 3

@login_required
def TeacherHome(request):
    template_name = "academic_feedback_sys/teacher_home.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        login_url = reverse('login') + '?' + urlencode({"next": request.path})
        redirect_login_response = redirect(login_url)
        redirect_login_response.set_cookie("session-cookie", "short-cookie")
        redirect_login_response.set_cookie("timed-cookie", "long-cookie", max_age=cookie_time)
        return redirect_login_response
    # create a context saving the teacher's object
    # can be gotten from request object easily
    # then return a response from the render object
    context_variable = {}
    logged_teacher_obj = request.user
    context_variable["logged_teacher_obj"] = logged_teacher_obj
    return render(request, template_name, context_variable)
