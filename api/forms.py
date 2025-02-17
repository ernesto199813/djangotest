# api/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # Use your custom user model or the default one
        fields = ('username', 'email', 'first_name', 'last_name') # Add desired fields