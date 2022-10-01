from django.urls import path
from . import views

urlpatterns = [
    path('userprofile', views.UserProfile, name='userprofile'),
]