from django import forms
from .models import Contacts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    pass

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ["name", "phone", "email", "city"]