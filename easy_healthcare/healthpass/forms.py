from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("first_name", "last_name", "email") + UserCreationForm.Meta.fields

class CustomLoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=300)
    password = forms.CharField(widget=forms.PasswordInput)
