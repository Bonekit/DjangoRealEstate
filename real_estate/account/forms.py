from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control', }), max_length=32)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control', }), max_length=32)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control', }), max_length=254)
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', }))
