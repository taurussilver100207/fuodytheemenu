from django.shortcuts import render, redirect
from .forms import *
from Home.models import *
from UserProfile.models import UserProfile
from django.contrib import messages
from Chat.models import *
# Create your views here.
def shop(request, id):
    shop = Shop.objects.get(id=id)
    room_name = f"{request.user.id}n{shop.user.id}"
    if request.method == "POST":
        accesoryForm = AccesoryForm(request.POST, request.FILES)
        if accesoryForm.is_valid():
            accesory = accesoryForm.save(commit=False)
            accesory.shop = shop
            accesory.save()
            return redirect('shop_home', id)
    else:
        accesoryForm = AccesoryForm()

    if request.user.is_authenticated:
        content = {
            'accesoryform': accesoryForm,
            'shop': shop,
            'userprofile': UserProfile.objects.get(user=request.user),
            'Accesory': Accesory.objects.all(),
            'userrealtime': shop.is_real_time.all(),
            'room_name': room_name
        }
    else:
        content = {
            'shop': shop,
        }       
    return render(request, 'shop/shop_home_page.html', content)


def create_order(request, id):
    accesory = Accesory.objects.get(id=id)
    order = Order.objects.create(
        user=request.user,
        accesory=accesory,
        price=accesory.price
    )
    
    messages.success(request, f"Your order {order.accesory.name} has been sent.")
    
    return redirect("shop_home", id=accesory.shop.id)

def is_realtime(request, id):
    shop = Shop.objects.get(id=id)
    shop.is_real_time.add(request.user)
    shop.save()
    return redirect("shop_home", id=shop.id)

def not_realtime(request, id):
    shop = Shop.objects.get(id=id)
    shop.is_real_time.remove(request.user)
    shop.save()
    return redirect("shop_home", id=shop.id)

def shop_order(request, id):
    userprofile = UserProfile.objects.get(user=request.user)
    shop = Shop.objects.get(id=id)
    orders = Order.objects.all()
    
    content = {
        'shop': shop,
        'orders': orders,
        'userprofile': userprofile
    }
    
    return render(request, "shop/orders.html", content)

def user_order(request):
    userprofile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.all()
    
    content = {
        'orders': orders,
        'userprofile': userprofile
    }
    
    return render(request, "shop/userorder.html", content)

def confirm_order(request, id):
    order = Order.objects.get(id=id)
    order.state = "Working"
    order.save()
    return redirect("shop_order", id=order.accesory.shop.id)

def finished_order(request, id):
    order = Order.objects.get(id=id)
    order.state = "Done"
    order.save()
    return redirect("shop_order", id=order.accesory.shop.id)

def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    
    return redirect("shop_order", id=order.accesory.shop.id)

def confirm_order_done(request, id):
    order = Order.objects.get(id=id)
    order.userconfirm = "Done"
    order.save()
    return redirect("user_order")

def follow(request, id):
    shop = Shop.objects.get(id=id)
    shop.followers.add(request.user)
    shop.save()
    
    return redirect('shop_home', id=id)

def unfollow(request, id):
    shop = Shop.objects.get(id=id)
    shop.followers.remove(request.user)
    shop.save()
    
    return redirect('shop_home', id=id)