from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ('email', 'first_name', 'last_name','username', 'password1', 'password2')

