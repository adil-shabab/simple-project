from django import forms
from django.forms import ModelForm, TextInput
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm








class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
        'username' : TextInput(attrs={'class': 'field rounded'}),
        'email' : TextInput(attrs={'class': 'field rounded'}),
        }