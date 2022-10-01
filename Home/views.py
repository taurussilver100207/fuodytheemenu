from django.shortcuts import render, redirect
from .forms import *
from UserProfile.models import *
from .models import *
# Create your views here.
def home(request):
    #Shop
    if request.method == "POST":
        shopform = ShopForm(request.POST, request.FILES)
        if shopform.is_valid():
            shop = shopform.save(commit=False)
            shop.user = request.user
            shop.save()
            return redirect('shop_home', id=shop.id)
    else:
        shopform = ShopForm()
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)
        shops = Shop.objects.all()
        content = {
            'shopform': shopform,
            'userprofile': userprofile,
            'Shops': shops,
        }
    else:
        content = {
            'shopform': shopform
        }
    return render(request, 'pages/home.html', content)
