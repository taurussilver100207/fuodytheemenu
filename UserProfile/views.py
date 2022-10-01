from django.shortcuts import render
from .forms import UserProfileForm
from django.http import HttpResponseRedirect
# Create your views here.
def UserProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            return HttpResponseRedirect('/')
    else:
        form = UserProfileForm()
    
    return render(request, 'pages/userprofile.html', { 'form': form })