from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authent.models.users import CustomUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, help_text="optional")
    last_name = forms.CharField(required=True, help_text="optional")
    email = forms.EmailField(required=True, help_text="Enter a valid")

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )

    class Meta:
        model: CustomUser
        fields = ["email", "password"]
