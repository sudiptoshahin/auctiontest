from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact_no = forms.CharField()
    address = forms.CharField()
    created_at = forms.DateTimeField(initial=datetime.now)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'contact_no', 'address']

