from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm

from authent.models.users import CustomUser


class PasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model: CustomUser
        fields = ["password"]

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
