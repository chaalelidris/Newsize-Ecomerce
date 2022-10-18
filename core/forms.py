from pickle import TRUE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=TRUE)
    last_name = forms.CharField(max_length=50, required=TRUE)
    email = forms.EmailField(max_length=255, required=TRUE)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]