from django.shortcuts import render,redirect
from common.models import Customer, Seller
from sellerpage.models import Product
from .models import Cart, Order, Order_details
from .auth_gaurd import auth_customer

# Create your views here.


@auth_customer
def cust_home(request):
    product_list = Product.objects.all()
    customer_data = Customer.objects.get(id=request.session['customer'])
    return render(request, 'customer/customer_home.html', {'data': customer_data, 'products': product_list})


@auth_customer
def my_profile(request):
    # seller_data = Seller.objects.get(id=request.session['seller'])
    # msg = ''
    # if request.method == 'POST':
    #     product_image = request.FILES['p_file']
    
    customer_data = Customer.objects.get(id=request.session['customer'])
    return render(request, 'customer/profile.html', {'data': customer_data})


@auth_customer
def cat(request):
    product_list = Product.objects.all()
    return render(request, 'customer/catalog.html', {'products': product_list})


@auth_customer
def changepass_cust(request):
    msg = ''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['cur_pass']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['conf_pass']

        if customer.customer_password == current_pass:

            if new_pass == confirm_pass:
                customer.customer_password = new_pass
                customer.save()
                msg = 'password change sucessful'

            else:
                msg = 'password does not match'   

        else:
            msg = 'incorect password'  
    context = {
        'msg':msg
    }              
    return render(request, 'customer/changepassword_cust.html',context)


@auth_customer
def my_cart(request):
    if 'customer' in request.session:  #customer is the key in session where customer login occurs
        # here we create an if 
        product_cart = Cart.objects.filter(customer = request.session['customer'])
        return render(request, 'customer/mycart.html',{'products':product_cart})
    else:
        return redirect('common:cuslog')    


@auth_customer
def product_detail(request, pid):
    product_list = Product.objects.all()
    msg = ''
    product_details = Product.objects.get(id=pid)

    if request.method == 'POST':
        
        #  checking if the user has added the same product in cart
        #  exist() methode return boolen value, tru if data exist , exist function only comes in filter not on get

        product_exist = Cart.objects.filter(product_d = pid,customer = request.session['customer']).exists()

        if not product_exist: # same as 'if product_exist == false'
            cart = Cart(customer_id = request.session['customer'],product_d_id = pid)
            cart.save()
        else:
            msg = 'item alredy add to cart'

        # data we pass views to template is called context data
    context = {
            'details': product_details,
            'msg':msg,
            'products': product_list
        }   
    return render(request, 'customer/productdetail.html',context)


@auth_customer
def remove_item(request,pid):
    cart_item = Cart.objects.get(product_d = pid,customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cart')


@auth_customer
def my_order(request):
    # user_id = request.session['customer'] 
    if 'customer' in request.session:  
        order = Order.objects.filter(customer_id = request.session['customer'])
        return render(request, 'customer/myorder.html',{'my_order':order})
    else:
        return redirect('common:cuslog')    


@auth_customer
def log_out(request):
    del request.session['customer']
    request.session.flush() #to remove session from django_session table
    return redirect('common:prohome')


@auth_customer
def master(request):
    pro=Product.objects.all()
    return render(request,'customer/masterpost.html',{'products':pro})


def purchase(request, pid):
    product_list = Product.objects.all()
    msg = ''
    product_details = Product.objects.get(id=pid)   

    if request.method == 'POST':
        

        order_exist = Order.objects.filter(product_id = pid,customer_id = request.session['customer']).exists()

        if not order_exist: 
            order = Order(customer_id_id = request.session['customer'],product_id_id = pid)
            order.save()
        else:
            msg = 'item alredy ordered'
        
    context = {
            'details': product_details,
            'msg':msg,
            'products': product_list
        }   
    return render(request, 'customer/purchase.html',context)
   

