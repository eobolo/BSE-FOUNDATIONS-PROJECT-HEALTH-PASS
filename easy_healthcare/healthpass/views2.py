from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.http import urlencode
from django.urls import reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms2 import DjangoUserCreationForm
# Create your views here.

"""utility functions"""
def normalize_data(first_name="", last_name=""):
    return first_name.capitalize(), last_name.capitalize()

class UserLogOut(View):
    template_name = "healthpass/logged_out.html"
    def get(self, request):
        return render(request, self.template_name)
    
class UserHome(View):
    template_name = "healthpass/user_home.html"
    def get(self, request):
        if request.user.is_authenticated:
            # TODO: make sure you do what is in the docstring
            """
            check if cookies is expired and redirect them login as
            get request and after authentication new cookies are added,
            and we are sent to user_home.
            """
            if not (request.COOKIES.get("user_session", None) == "session_cookie") or \
                    not (request.COOKIES.get("user_time", None) == "time_cookie"):
                login_url = reverse("login") + "?" + urlencode({"next": request.path})
                response = redirect(login_url)

                # set seesion cookie that will expire if browser is closed
                response.set_cookie("user_session", "session_cookie", max_age=None)

                #set time cookie that will expire after about 2hours in seconds
                response.set_cookie("user_time", "time_cookie", max_age=7200)

                # redirect the response
                return response

            """
            we need to know the user authenticated either django user
            or custom user.
            """
            if not isinstance(request.user, User):
                login_url = reverse("login") + "?" + urlencode({"next": request.path})
                response = redirect(login_url)

                # set seesion cookie that will expire if browser is closed
                response.set_cookie("user_session", "session_cookie", max_age=None)

                #set time cookie that will expire after about 2hours in seconds
                response.set_cookie("user_time", "time_cookie", max_age=7200)

                # redirect the response
                return response

            """
            If both case come out False render the custom home page
            will add some context soon.
            """
            # create context variable
            context = {}
            context['user'] = request.user

            # return context variable with request and template name
            return render(request, self.template_name, context)

        # if user is not authenticated
        login_url = reverse("login") + "?" + urlencode({"next": request.path})
        response = redirect(login_url)

        # set session cookie that will expire if browser is closed
        response.set_cookie("user_session", "session_cookie", max_age=None)

        #set time cookie that will expire after about 2hours in seconds
        response.set_cookie("user_time", "time_cookie", max_age=7200)

        # redirect the response
        return response

class UserSignUp(View):
    template_name = "healthpass/django_user.html"
    def get(self, request):
        # now get the django user creation form from forms2.py
        djangouser_form = DjangoUserCreationForm
        # now store this in context variable
        context = {}
        context["djangouser_form"] = djangouser_form
        # now render the form from models in a template
        return render(request, self.template_name, context)

    def post(self, request):
        # create context variable
        context = {}
        # get the result of the post request form and check if it is valid
        check_djangouser_form = DjangoUserCreationForm(request.POST)
        if not check_djangouser_form.is_valid():
            message = "Unable to submit form, validation wrong!!!"
            context["djangouser_form"] = check_djangouser_form
            context["error_message_1"] = message
            return render(request, self.template_name, context)
        # now check for the following validation
        # before model can be saved.
        # check if first name and lastname already exist
        check_first_name = request.POST.get("first_name")
        check_last_name = request.POST.get("last_name")
        names_bool = User.objects.filter(
            first_name=check_first_name,
            last_name=check_last_name,
        ).exists();
        if names_bool:
            message = f"User with the names {check_first_name} {check_last_name} already exists"
            djangouser_form = DjangoUserCreationForm()
            context["djangouser_form"] = djangouser_form
            context["error_message"] = message
            return render(request, self.template_name, context)
        # check if the username already exist although .is_valid check this for us
        check_username = request.POST.get("username")
        username_bool = User.objects.filter(
            username=check_username,
        ).exists()
        if username_bool:
            message = f"User with the username {check_username} already exists"
            djangouser_form = DjangoUserCreationForm()
            context["djangouser_form"] = djangouser_form
            context["error_message"] = message
            return render(request, self.template_name, context)
        # check if the email already exist
        check_email = request.POST.get("email")
        email_bool = User.objects.filter(
            email=check_email,
        ).exists()
        if email_bool:
            message = f"User with the email {check_email} already exists"
            djangouser_form = DjangoUserCreationForm()
            context["djangouser_form"] = djangouser_form
            context["error_message"] = message
            return render(request, self.template_name, context)
        # check if the both password1 and password2 are the same althougth .is_valid does that
        password_1 = request.POST.get("password1")
        password_2 = request.POST.get("password2")
        if password_1 != password_2:
            message = f"password_1 and password_2 do not match!!!"
            djangouser_form = DjangoUserCreationForm()
            context["djangouser_form"] = djangouser_form
            context["error_message"] = message
            return render(request, self.template_name, context)

        # now let us normalize the names  before saving
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        first_name, last_name = normalize_data(
            first_name=first_name,
            last_name=last_name,
        )
        # now make a copy of the request.POST
        request_post_mutable = request.POST.copy()
        # change the mutable post request data with these normalized ones
        request_post_mutable["first_name"] = first_name
        request_post_mutable["last_name"] = last_name

        # create a form object from customusercreationform using the request.post data
        # and save it password hashing is been taken care of.
        # email normalization and is_active is set to true
        save_djangouser_data = DjangoUserCreationForm(request_post_mutable)
        save_djangouser_object = save_djangouser_data.save(commit=False)
        save_djangouser_object.save()

        # now send them to our django built in login
        login_url = reverse("login") + "?" + urlencode({"next": reverse("health:user_home")})
        
        # put a flash message also indicating user created
        messages.success(request, "DjangoUser Data saved.")
        response = redirect(login_url)

        # set seesion cookie that will expire if browser is closed
        response.set_cookie("user_session", "session_cookie", max_age=None)

        # set time cookie that will expire after about 2hours in seconds
        response.set_cookie("user_time", "time_cookie", max_age=7200)

        # return response object
        return response
