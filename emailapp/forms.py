from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Email

class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

class ComposeForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('subject', 'body')
