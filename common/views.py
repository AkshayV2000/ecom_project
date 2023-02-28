from django.shortcuts import render, redirect
from .models import Customer, Seller
from sellerpage.models import Product
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.


def p_home(request):
    product_list = Product.objects.all()
    return render(request, 'common/project_home.html', {'products': product_list})


def c_home(request):
    mss = ''
    if request.method == 'POST':
        cust_email = request.POST['cust_mail']
        cust_password = request.POST['cust_pass']

        try:
            customer = Customer.objects.get(
                customer_email = cust_email, customer_password = cust_password)
            request.session['customer'] = customer.id  # create a session
            return redirect('customer:customer_home')
        except :
            mss = 'email and password is incorrect'
            return render(request, 'common/cust_login.html', {'mss': mss, })
    return render(request, 'common/cust_login.html')


def c_signup(request):

    if request.method == 'POST':
        cst_name = request.POST['c_name']
        cst_email = request.POST['c_mail']
        cst_password = request.POST['c_pass']
        cst_number = request.POST['nub']
        cst_address = request.POST['c_address']
        cst_gender = request.POST['gender']
        # to insert6 data into table

        # 1.create object of model class eg: customer

        new_customer = Customer(customer_name=cst_name,
                                customer_email=cst_email,
                                customer_password=cst_password,
                                customer_addres=cst_address,
                                customer_gender=cst_gender)

        new_customer.save()

    return render(request, 'common/cust_signup.html')


def s_home(request):
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['u_name']
        pass_word = request.POST['pass']

        try:
            seller = Seller.objects.get(
                seller_username=user_name,  seller_password=pass_word)

        #  if username and password correct,we set a session variable with key 'seller'
        # session variable will be accessed throughout the application

        # working of django session
        # when username and password correct,we set a session variable with key(here key is 'seller') and
        # unique value for each seller (here value is the primary key of the logged in seller)
        # if a seller with primary key 2 logs in, session key will be 'seller' and value will be 2

        # when we set a session, key and value will be stored in django_session table inside database in encrypted from

        # the encrypted key will be sent with http response to the clinte (browser)
        # in the clinte side (browser), the key reciver from the server will be stored in browser storage (cookies in case of django)

        # when the user request any opage (eg : cart page) from the same browser, the sme key stored inside cookies
        # will be send to the server through http request

        # when request reches the server, it will look for the key stored in cookies to match with
        # django_session table inside the database to find the corresponding user

            request.session['seller'] = seller.id  # create a session
            return redirect('sellerpage:sellerhome')
        except:
            msg = 'username and password is incorrect'
    return render(request, 'common/seller_login.html', {'msg': msg, })


def s_signin(request):
    if request.method == 'POST':
        seller_name = request.POST['s_name'].lower()
        seller_address = request.POST['s_address']
        seller_phone = request.POST['s_phone']
        seller_email = request.POST['s_email']
        seller_companyname = request.POST['s_companyname']
        seller_holdername = request.POST['s_accholdername']
        seller_ifsc = request.POST['s_ifsc']
        seller_branch = request.POST['s_branch']
        seller_accno = request.POST['s_accnumber']
        seller_file = request.FILES['s_file']

        seller_username = random.randint(1111, 9999)
        seller_password = 'sel-' + seller_name + str(seller_username)
        message = 'hai your username is ' + \
            str(seller_username) + 'and temporary password is ' + seller_password
        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email,],
            fail_silently=False
        )

        new_seller = Seller(
            seller_name=seller_name,
            seller_address=seller_address,
            seller_email=seller_email,
            seller_phone=seller_phone,
            seller_companyname=seller_companyname,
            seller_accholdername=seller_holdername,
            seller_ifsc=seller_ifsc,
            seller_branch=seller_branch,
            seller_accno=seller_accno,
            seller_pic=seller_file,
            seller_password=seller_password,
            seller_username=seller_username,

        )

        new_seller.save()

    return render(request, 'common/seller_signin.html')

def email_exist(request):
    email = request.POST['email'] # here 'email' is the key in json

    status = Customer.objects.filter(customer_email = email).exists()

    return JsonResponse({'status':status}) 