from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django import forms

class CustomPasswordResetForm(PasswordResetForm):
    pass

class CustomSetPasswordForm(SetPasswordForm):
    pass

class CustomPasswordCheck(forms.Form):
    new_password1 = forms.CharField(label='New Password', required=True,  widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError("The two password fields didn't match.")

        return cleaned_data
