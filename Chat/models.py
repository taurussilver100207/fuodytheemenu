from importlib.resources import contents
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    members = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room.name