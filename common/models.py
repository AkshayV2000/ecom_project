from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=20)
    customer_password = models.CharField(max_length=10)
    customer_addres = models.CharField(max_length=40,default='')
    customer_gender = models.CharField(max_length=40,default='')


class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    seller_address = models.CharField(max_length=100)
    seller_phone = models.BigIntegerField()
    seller_email = models.CharField(max_length=30)
    seller_companyname = models.CharField(max_length=20)
    seller_accholdername = models.CharField(max_length=20)
    seller_ifsc = models.CharField(max_length=15)
    seller_branch = models.CharField(max_length=20)
    seller_accno = models.BigIntegerField()
    seller_username = models.CharField(max_length=20)
    seller_password = models.CharField(max_length=20)
    seller_pic = models.ImageField(upload_to='seller/')
    approved = models.BooleanField(default=False)
