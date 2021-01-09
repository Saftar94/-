from .models import Name
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['title', 'password']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),


            'password ': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
