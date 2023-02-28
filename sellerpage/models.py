from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=70)
    product_discription = models.CharField(max_length=800,default='')
    product_number = models.BigIntegerField()
    product_catogari = models.CharField(max_length=20,default='')
    product_stock = models.IntegerField()
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to="product")