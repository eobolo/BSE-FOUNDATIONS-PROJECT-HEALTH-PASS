from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("first_name", "last_name", "email") + UserCreationForm.Meta.fields

class CustomLoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=300, help_text="Enter your username or email")
    password = forms.CharField(help_text="Enter your password", widget=forms.PasswordInput)
