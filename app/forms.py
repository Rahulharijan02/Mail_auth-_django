from django.forms import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    email = forms.EmailField(max_length=200, widget=forms.EmailInput(
        attrs={'class':'form-control'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']