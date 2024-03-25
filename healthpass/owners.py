from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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
            messages.success(self.request, f"User {self.model.__name__} details :)")
            return qs
        messages.error(self.request, f"No data found for User {self.model} :(")
        return qs
