from django.views.generic.list import ListView
from .models import BloodWork, GeneralInfo, Urinalysis
from django.contrib.auth.models import User
# create your views here

class CustomBloodWorkListView(ListView):
    model = BloodWork
    template_name = "healthpass/custom_bloodwork_list.html"
    paginate_by = 3

    def get_queryset(self):

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


