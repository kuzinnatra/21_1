from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from django import forms
from catalog.forms import StyleFormMixin
from users.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    """Форма для сброса пароля"""
    class Meta:
        model = User
        fields = ['email', ]

