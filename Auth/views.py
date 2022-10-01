from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
            auth_login(request, new_user)
            return redirect('/userprofile')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'There was a logging in. Please try again.')
            return redirect('/auth/login')
    
    return render(request, 'auth/login.html')
    
    
