from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="chat_index"),
    path('<str:room_name>/', views.room, name="room"),
    path('shopchat/<int:user_id>', views.shop_chat, name="shop_chat")
]
