from django.db import models
from sellerpage.models import Product
from common.models import Customer
from datetime import date
# Create your models here.

class Cart(models.Model):
    product_d = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    price = models.FloatField()
    status = models.CharField(max_length=30,default='pending')
    seller_id = models.CharField(max_length=40)
    payment_id = models.CharField(max_length=35)


class Order_details(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=30,default='pending')
    payment_id = models.CharField(max_length=35)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
  

# class Profile(models.Model):
#     profile_pic = models.ImageField(upload_to="product")