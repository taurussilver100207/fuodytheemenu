from ast import type_ignore
from django.shortcuts import render
from .models import *
from UserProfile.models import *
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    room = Room.objects.filter(name=room_name).first()
    chats = []
    if room:
        chats = Chat.objects.filter(room=room)
    else:
        room = Room.objects.create(name=room_name)
        pre_userarray = room.name.split("n")
        userarray = []
        for i in pre_userarray:
            userarray.append(int(i))
        user1 = User.objects.get(id=userarray[0])
        user2 = User.objects.get(id=userarray[1])
        room.members.add(user1)
        room.members.add(user2)
        room.save()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'chats': chats,
        'userprofiles': UserProfile.objects.all(),
        'room': room,
        'rooms': Room.objects.all()
    })

def shop_chat(request, user_id):
    return render(request, 'chat/chat_home_page.html', {
        'shopuser': User.objects.get(id=user_id),
        'userprofiles': UserProfile.objects.all(),
        'rooms': Room.objects.all()
    })