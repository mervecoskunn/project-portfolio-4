from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, password_validation


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        "type": "text",
        "class": "form-control",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "type": "password",
            "class": "form-control",
            "placeholder": "Enter your password"
        }),
    )


class RegisterForm(BaseUserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        "type": "text",
        "class": "form-control",
        "placeholder": "Enter your username"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "autofocus": True,
        "type": "email",
        "class": "form-control",
        "placeholder": "Enter your email"
    }))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "type": "password",
            "class": "form-control",
            "placeholder": "Enter your new password"
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "type": "password",
            "class": "form-control",
            "placeholder": "Enter your new password again"
        }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)
