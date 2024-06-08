from django import forms

class ParentViewForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name"}),
    )
    middle_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Enter your middle name"}),
    )
    last_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Enter your last name"}),
    )
    password = forms.UUIDField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your uuid password"}),
    )
