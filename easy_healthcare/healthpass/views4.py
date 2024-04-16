from django.views.generic.list import ListView
from .models import BloodWork, GeneralInfo, Urinalysis
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CustomUser
# create your views here

class CustomBloodWorkListView(ListView):
    model = BloodWork
    template_name = "healthpass/custom_bloodwork_list.html"
    paginate_by = 3
    context_object_name = "bloodwork_list"

    def get_queryset(self):
        if 'page' in self.request.GET:
            return super().get_queryset()

        """
        get the base query set based on the model
        because this is what we would filter
        if filter queries are given i.e
        first_name, last_name, and email.
        """
        base_query_set = super().get_queryset()

        # make a copy of the request.GET
        get_request_copy = self.request.GET.copy()

        # filter the request for empty string values
        get_request_copy = {
            key: value for key, value in get_request_copy.items() if value != ""
        }
        # check if no search filter was sent at all
        if not get_request_copy:
            # save a session message for me
            self.request.session["filter"] = "no search"
            # now return base_query_set
            return base_query_set
        
        # if there is at least a single search filter
        # capitalize first_name, last_name for normalization search
        # if they exist in the get_request_copy
        get_request_copy = {
            key: value.capitalize() if key == "first_name" or key == "last_name" \
                    else value for key, value in get_request_copy.items() 
        }

        # now use the get_request_copy to filter the django user
        # objects with the filter either first_name, last_name, or email
        django_user_objs = User.objects.filter(**get_request_copy).all()

        # now use this django_user_objs to filter the base_query_set
        base_query_set = base_query_set.filter(owner__in=django_user_objs)

        # save a session message for me
        self.request.session["filter"] = "search"

        # return search base_query_set
        return base_query_set

    def get_context_data(self, **kwargs):
        if 'page' in self.request.GET:
            self.object_list = self.get_queryset()
            return super().get_context_data(**kwargs)
        # first save an object_list to self.get_queryset()
        # this is because I overwrote the get(self, request, *args, **kwargs) method
        # but if you don't it is not needed.
        self.object_list = self.get_queryset()

        # check if query set is empty due to search
        # or no search
        base_query_set = self.get_queryset()

        # get the context data
        context = super().get_context_data(**kwargs)

        # check for search
        if self.request.session["filter"] == "search":
            if not base_query_set:
                context["search_message"] = "No result found on this user(s)"
                del self.request.session["filter"]

        elif self.request.session["filter"] == "no search":
            if not base_query_set:
                context["search_message"] = "No result found on any user"
                del self.request.session["filter"]
        return context

    def get(self, request, *args, **kwargs):
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
            # get context data if search was done
            context = self.get_context_data(**kwargs)
            # now render result
            return render(request, self.template_name, context)
        login_url = reverse("health:custom_login")
        return redirect(login_url)

class CustomGeneralInfoListView(CustomBloodWorkListView):
    model = GeneralInfo
    template_name = "healthpass/custom_generalinfo_list.html"
    context_object_name = "generalinfo_list"

class CustomUrinalysisListView(CustomGeneralInfoListView):
    model = Urinalysis
    template_name = "healthpass/custom_urinalysis_list.html"
    context_object_name = "urinalysis_list"
