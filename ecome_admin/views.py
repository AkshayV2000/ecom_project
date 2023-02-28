from django.shortcuts import render,redirect
from common.models import Customer,Seller
from sellerpage.models import Product
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def ecomadmin_home(request):
    product = Product.objects.all()
    return render(request,'ecome_admin/admin_home.html',{'product_list':product})

def approve_cust(request):

    customer = Customer.objects.all()

    return render(request,'ecome_admin/approvecust.html',{'customer_list':customer})

def approve_seller(request):
    seller = Seller.objects.all()
    return render(request,'ecome_admin/approveseller.html',{'seller_list':seller})


def view_cust(request):
    cust = Customer.objects.all()
    return render(request,'ecome_admin/view_cust.html',{'cust_list':cust})

def view_seller(request):
    sell = Seller.objects.filter(approved = True)
    return render(request,'ecome_admin/viewseller.html',{'sell_list':sell})

def approve(request,sid):
    seller = Seller.objects.get(id=sid)
    msg = 'you are approved to login'
    send_mail(
        'login approve',
        msg,
        settings.EMAIL_HOST_USER,
        [seller.seller_email,],
    )
    seller.approved = True
    seller.save()
    return redirect('ecom_admin:approveseller')


def delete_seller(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('ecom_admin:approveseller')

def delete_cust(request,sid):
    customer_list = Customer.objects.get(id = sid)
    customer_list.delete()
    return redirect('ecom_admin:approvecust')    