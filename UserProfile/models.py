from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Not to mention", "Not to mention")
)

USERTYPE = (
    ("Customer", "Customer"),
    ("Shop owner", "Shop owner"),
)


class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="Male")
    usertype = models.CharField(max_length=20, choices=USERTYPE, default="Customer")
    avatar = models.ImageField(null=True, blank=True, upload_to = "images/")
    
    def __str__(self):
        return self.user.username