from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.http import urlencode
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUser
# Create your views here.

"""utility functions"""
def normalize_data(first_name="", last_name=""):
    return first_name.capitalize(), last_name.capitalize()

class CustomHome(View):
    template_name = "healthpass/custom_home.html"
    def get(self, request):
        if request.user.is_authenticated:
            # TODO: make sure you do what is in the docstring
            """
            check if cookies is expired and redirect them login as
            get request and after authentication new cookies are added,
            and we are sent to custom_home.
            """
            if not (request.COOKIES.get("custom_session", None) == "session_cookie") or \
                    not (request.COOKIES.get("custom_time", None) == "time_cookie"):
                login_url = reverse("health:custom_login")
                return redirect(login_url)
            """
            we need to know the user authenticated either django user
            or custom user.
            """
            if not isinstance(request.user, CustomUser):
                login_url = reverse("health:custom_login")
                return redirect(login_url)

            """
            If both case come out False render the custom home page
            will add some context soon.
            """
            return render(request, self.template_name)
        login_url = reverse("health:custom_login")
        return redirect(login_url)

class CustomSignUp(View):
    template_name = "healthpass/custom_user.html"
    def get(self, request):
        # now get the custom user creation form from forms.py
        customuser_form = CustomUserCreationForm()
        # now store this in context variable
        context = {}
        context["customuser_form"] = customuser_form
        # now render the form from models in a template
        return render(request, self.template_name, context)

    def post(self, request):
        # create context variable
        context = {}
        # get the result of the post request form and check if it is valid
        check_customuser_form = CustomUserCreationForm(request.POST)
        if not check_customuser_form.is_valid():
            message = "Unable to submit form, validation wrong!!!"
            context["customuser_form"] = check_customuser_form
            context["error_message_1"] = message
            return render(request, self.template_name, context)
        # now check for the following validation
        # before model can be saved.
        # check if first name and lastname already exist
        check_first_name = request.POST.get("first_name")
        check_last_name = request.POST.get("last_name")
        names_bool = CustomUser.objects.filter(
            first_name=check_first_name,
            last_name=check_last_name,
        ).exists();
        if names_bool:
            message = f"User with the names {check_first_name} {check_last_name} already exists"
            customuser_form = CustomUserCreationForm()
            context["customuser_form"] = customuser_form
            context["error_message"] = message
            return render(request, self.template_name, context)
        # check if the username already exist
        check_username = request.POST.get("username")
        username_bool = CustomUser.objects.filter(
            username=check_username,
        ).exists()
        if username_bool:
            message = f"User with the username {check_username} already exists"
            customuser_form = CustomUserCreationForm()
            context["customuser_form"] = customuser_form
            context["error_message"] = message
            return render(request, self.template_name, context)
        # check if the email already exist
        check_email = request.POST.get("email")
        email_bool = CustomUser.objects.filter(
            email=check_email,
        ).exists()
        if email_bool:
            message = f"User with the email {check_email} already exists"
            customuser_form = CustomUserCreationForm()
            context["customuser_form"] = customuser_form
            context["error_message"] = message
            return render(request, self.template_name, context)
        # check if the both password1 and password2 are the same
        password_1 = request.POST.get("password1")
        password_2 = request.POST.get("password2")
        if password_1 != password_2:
            message = f"password_1 and password_2 do not match!!!"
            customuser_form = CustomUserCreationForm()
            context["customuser_form"] = customuser_form
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
        save_customuser_data = CustomUserCreationForm(request_post_mutable)
        save_customuser_object = save_customuser_data.save(commit=False)
        save_customuser_object.is_active = True
        save_customuser_object.save()

        # now send them to our customlogin
        login_url = reverse("health:custom_login")
        
        # put a flash message also indicating user created
        messages.success(request, "CustomUser Data saved.")
        return redirect(login_url)

class CustomLogin(View):
    # this template_name would be over written in the urls.py
    template_name = None
    # define the get request to this view
    def get(self, request):
        # create the custom login form
        custom_login_form = CustomLoginForm()
        # create the context variable to take this form object
        context = {}
        context["custom_login_form"] = custom_login_form
        return render(request, self.template_name, context)

    def post(self, request):
        # get the username_email and password first
        username_or_email = request.POST.get("username_or_email")
        password = request.POST.get("password")

        # now we have to authenticate using our already defined CustomBackend class
        authenticate_user = authenticate(
                request,
                username_or_email=username_or_email,
                password=password,
        )
        # check if the authenticated user is not None
        if authenticate_user is not None:
            # check to see that custom user is not active
            # then make the user active
            if authenticate_user.is_active:
                # log the custom user in
                login(request, authenticate_user)
                # display a flash message for successful login
                messages.success(request, "CustomUser logged in...")
                
                # TODO: make sure you do what is in the docstring
                """
                before you redirect custom_home add cookies to it.
                session cookies, and time period cookies.
                """
                response = redirect(reverse("health:custom_home"))

                # set seesion cookie that will expire if browser is closed
                response.set_cookie("custom_session", "session_cookie", max_age=None)

                #set time cookie that will expire after about 2hours in seconds
                response.set_cookie("custom_time", "time_cookie", max_age=7200)

                # redirect the custom user to the custom_home
                return response
            else:
                # redirect to the user has been blocked
                return redirect(reverse("health:custom_ban"))
        context = {}
        custom_login_form = CustomLoginForm(request.POST)
        context["custom_login_form"] = custom_login_form
        message = "Incorrect details password or username_email wrong"
        context["error_message"] = message
        return render(request, self.template_name, context)

class CustomLogout(View):
    # no template is being rendered
    # just logout the current user using the logout function
    # then redirect to a success page in this case back to the custom login
    def get(self, request):
        # logout the current user using logout(request) function
        logout(request)
        # add a flash message to the login file to indicate login succesful
        messages.success(request, "CustomUser successfully logged out :)")
        # then redirect success page i.e out custom login
        return redirect(reverse("health:custom_login"))
