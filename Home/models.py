from io import BytesIO
from tkinter import Image
from django.db import models
from django.contrib.auth.models import User
import random
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.
ORDERSTATE = (
    ("Waiting", "Waiting"),
    ("Working", "Working"),
    ("Done", "Done"),
)
def random_string():
    return str(random.randint(10000, 99999))    
    
class Shop(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to = "images/")
    is_real_time = models.ManyToManyField(User)
    followers = models.ManyToManyField(User, related_name='followers')
    qr_code = models.ImageField(null=True, blank=True, upload_to = "images/")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Accesory(models.Model):
    shop = models.ForeignKey(Shop, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to = "images/")
    price = models.IntegerField()
    
    def __str__(self):
        return self.shop.name

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="orderer")
    accesory = models.ForeignKey(Accesory, null=True, on_delete=models.CASCADE, related_name="accesory")
    price = models.IntegerField()
    num = models.IntegerField(default=random_string())
    state = models.CharField(max_length=20, choices=ORDERSTATE, default="Waiting")
    userconfirm = models.CharField(max_length=20, choices=ORDERSTATE, default="Waiting")
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.accesory.name