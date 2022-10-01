from django.urls import path
from . import views

urlpatterns = [
    path('home/<int:id>', views.shop, name="shop_home"),
    path('create_order/<int:id>', views.create_order, name="create_order"),
    path('is_realtime/<int:id>', views.is_realtime, name="is_realtime"),
    path('not_realtime/<int:id>', views.not_realtime, name="not_realtime"),
    path('order/<int:id>', views.shop_order, name="shop_order"),
    path('confirm_order/<int:id>', views.confirm_order, name="confirm_order"),
    path('finished_order/<int:id>', views.finished_order, name="finished_order"),
    path('delete_order/<int:id>', views.delete_order, name="delete_order"),
    path('confirm_order_done/<int:id>', views.confirm_order_done, name="confirm_order_done"),
    path('userorder', views.user_order, name="user_order"),
    path('follow/<int:id>', views.follow, name="follow"),
    path('unfollow/<int:id>', views.unfollow, name="unfollow")
]