from random import choices
from django import forms
from .models import *
from Home.models import *
from .views import *

class AccesoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs= {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
    }))
    price = forms.CharField(widget=forms.NumberInput(attrs= {
        'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-600 focus:ease-in-out delay-150 duration-300',
    }))
    image = forms.FileField(widget=forms.FileInput(attrs = {
        'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-200 file:text-violet-700 hover:file:bg-violet-300',
        "accept": "image/*"
    }))
    class Meta:
        model = Accesory
        fields = [
            'name',
            'price',
            'image'
        ]