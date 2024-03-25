from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse

class OWNERCREATEVIEW(LoginRequiredMixin, CreateView):
    # overwrite the form_valid function
    def form_valid(self, form):
        # get the form save it and don't commit it to the database
        # and now return the model object and add the user authenticated to the owner field
        model_object = form.save(commit=False)
        model_object.owner = self.request.user
        # now save the model_object temporarily and it would save permanently
        # if validation is correct
        model_object.save()
        # return the super class form validation
        return super(OWNERCREATEVIEW, self).form_valid(form)

    def get_success_url(self):
        # also add a flash message
        messages.success(self.request, f"{self.model.__name__} form saved.")
        # Redirect to the same page after form submission
        return self.request.path

class OWNERLISTVIEW(LoginRequiredMixin, ListView):
    # get the list of the specific logged in user data
    # using get query set and add flash messages if it sees it or not
    def get_queryset(self):
        qs = super(OWNERLISTVIEW, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        # save both error and success messages based on the value of qs
        if qs:
            messages.success(self.request, f"{self.model.__name__} data found for {self.request.user.first_name} :)")
            return qs
        messages.error(self.request, f"No {self.model.__name__} data found for {self.request.user.first_name} :(")
        return qs

class OWNERUPDATEVIEW(LoginRequiredMixin, UpdateView):
    # get the list of the specific logged in user data
    # using the get query set that also searches using the model and
    # the url parameter given i.e the id of the object
    def get_queryset(self):
        qs = super(OWNERUPDATEVIEW, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        # save both error and success message based of the value of qs
        # if there is an object of that id found and also belongs to the owner
        # note after the get request is valid updateview populates the form with the object found as old data
        if qs:
            messages.success(self.request, f"{self.model.__name__} data found for {self.request.user.first_name} and can be updated :)")
            return qs
        messages.error(self.request, f"No {self.model.__name__} data found for {self.request.user.first_name} :(")
        return qs

    # now check if the form is valid if data is found after being submitted
    def form_valid(self, form):
        # get the form and save it and don't commit it to the database.
        # and now return the model object and add the user authenticated to the owner field
        model_object = form.save(commit=False)
        model_object.owner = self.request.user
        # now save the model_object temporarily and it would save permanently
        # if validation is correct
        # return the super class form validation
        return super(OWNERUPDATEVIEW, self).form_valid(form)

    # if the form has been updated and save to the database for that blood work id for that specified user
    # redirect a success url to the same update form path
    def get_success_url(self):
        # also add a flash message
        messages.success(self.request, f"{self.model.__name__} form update saved.")
        # Redirect to the same page after form submission
        return self.request.path

class OWNERDELETEVIEW(LoginRequiredMixin, DeleteView):
    # get the list of the specific logged in user data
    # using the get query set that also searches using the model and
    # the url parameter given i.e the id of the object
    def get_queryset(self):
        qs = super(OWNERDELETEVIEW, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        # save both error and success message based of the value of qs
        # if there is an object of that id found and also belongs to the owner
        # now you need a confirm delete template to assure delete by the generic deleteview
        if qs:
            messages.success(self.request, f"{self.model.__name__} data found for {self.request.user.first_name} and can be deleted :)")
            return qs
        messages.error(self.request, f"No {self.model.__name__} data found for {self.request.user.first_name} :(")
        return qs

    def get_success_url(self):
        # also add a flash message
        messages.success(self.request, f"{self.model.__name__} data deleted succesfully :)")
        # Redirect to the same page after form submission
        if self.model.__name__ == "BloodWork":
            return reverse("health:blood_work_read_delete")
        elif self.model.__name__ == "GeneralInfo":
            pass
        else:
            pass
