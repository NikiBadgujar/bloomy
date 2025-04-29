from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')
    is_on_sale=models.BooleanField(default=False)
    sale_price= models.DecimalField(max_digits=10, decimal_places=2,default=False)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
            return f'{self.quantity} x {self.flower.name}'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone=models.CharField(max_length=10)
    address=models.TextField(max_length=700)
    cart = models.JSONField(null=True)
    status=models.CharField(max_length=20,default='pending')
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    