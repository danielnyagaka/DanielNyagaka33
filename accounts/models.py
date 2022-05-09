from django.db import models
from django.contrib.auth.models import User
from shop.models import Product,Category


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    phone=models.IntegerField(default=+917447650728)
    is_verified = models.BooleanField(default=False)
    forget_password_token = models.CharField(max_length=100,default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


class Wishlist(models.Model):
    wish_id= models.AutoField(primary_key=True,default='999')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    wish_prod=models.CharField(max_length=250, unique=True,default='ads123')
    
    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=1000, default="")


    def __str__(self):
        return self.name
