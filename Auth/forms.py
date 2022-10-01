from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
        'id': 'grid-first-name',
        'placeholder': 'John'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
        'id': 'grid-last-name',
        'placeholder': 'Doe'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
        'placeholder': 'you@example.com',
        'id': 'grid-email'
    }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
        'placeholder': 'e.g. jdoe',
        'id': 'grid-username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
        'placeholder': '********',
        'id': 'grid-password'
    }))
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Your username is using special characters.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Itami Account already exists')
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Your password must be longer than 8 characters')
        else:
            return password

    def save(self):
        User.objects.create_user(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            username=self.cleaned_data['username'], 
            email=self.cleaned_data['email'], 
            password=self.cleaned_data['password'])