from django import forms

class ParentViewForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(),
    )
    middle_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(),
    )
    last_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(),
    )
    password = forms.UUIDField(
        required=True,
        widget=forms.PasswordInput(),
    )
