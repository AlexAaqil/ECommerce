from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserSignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username", "class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"Email Address", "class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter a Password", "class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm your Password", "class":"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email']