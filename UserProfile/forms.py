from django import forms
from .models import UserProfile ,GENDER, USERTYPE
from django.core.exceptions import ObjectDoesNotExist
class UserProfileForm(forms.ModelForm):
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', widget=forms.NumberInput(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
        'placeholder': 'e.g. 0999999999'
    }))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300 pl-10 p-2.5',
        'datepicker': 'True',
        'placeholder': 'Select date'
    }))
    gender = forms.ChoiceField(choices = GENDER ,widget=forms.Select(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300'
    }))
    usertype = forms.ChoiceField(choices = USERTYPE ,widget=forms.Select(attrs = {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300'
    }))
    avatar = forms.ImageField(widget=forms.FileInput(attrs = {
       'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-200 file:text-violet-700 hover:file:bg-violet-300',
       "accept": "image/*"
   }))
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            UserProfile.objects.get(phone_number=phone_number)
        except ObjectDoesNotExist:
            return phone_number
        raise forms.ValidationError('The phone number has been used.')
        
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'birthdate', 'gender', 'avatar', 'usertype']
        