from django.shortcuts import render, redirect
from common.models import Seller
from .models import Product
from django.http import JsonResponse
from .auth_gaurd import auth_seller


# Create your views here.

@auth_seller
def sl_h(request):
    product_list = Product.objects.all()
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'sellerpage/seller_home.html', {'data': seller_data,'products': product_list})

@auth_seller
def add_pro(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    msg = ''
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_discription = request.POST['p_dis']
        product_number = request.POST['p_no']
        product_catogary = request.POST['catogary']
        product_price = request.POST['p_price']
        product_stock = request.POST['P_stock']
        product_image = request.FILES['p_file']

        new_product = Product(

            product_name=product_name,
            product_discription=product_discription,
            product_number=product_number,
            product_catogari=product_catogary,
            product_stock=product_stock,
            product_price=product_price,
            product_image=product_image,
            seller_id=request.session['seller']

        )
        new_product.save()
        msg = 'product added sucessfully'
    return render(request, 'sellerpage/add_product.html', {'msg': msg, 'data': seller_data})

@auth_seller
def cato_log(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    seller_products = Product.objects.filter(seller=request.session['seller'])
    return render(request, 'sellerpage/catalog_seller.html', {'products': seller_products, 'data': seller_data})

@auth_seller
def change_pass(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    msg = ''
    if request.method == 'POST':
        seller = Seller.objects.get(id=request.session['seller'])

        current_pass = request.POST['cur_pass']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['conf_pass']

        if seller.seller_password == current_pass:

            if new_pass == confirm_pass:
                # Seller.objects.filter( ).update(current_pass = new_pass)
                seller.seller_password = new_pass
                seller.save()
                msg = 'password change successfully'

            else:
                msg = 'password does not match'

        else:
            msg = 'incorect password'
        
    context = {
        'msg': msg,
        'data': seller_data,
    }
    return render(request, 'sellerpage/change_password.html', context)

@auth_seller
def od_history(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'sellerpage/order_history.html', {'data': seller_data})

@auth_seller
def r_history(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'sellerpage/recent_history.html', {'data': seller_data})

@auth_seller
def s_update(request):
    msg = ''
    seller_data = Seller.objects.get(id=request.session['seller'])

    product_stock = Product.objects.filter(seller=request.session['seller'])
    if request.method == 'POST':
        new_stock = request.POST['new_stock']
        product_id = request.POST['pro_id']

        product = Product.objects.get(id=product_id)

        product.product_stock = product.product_stock + int(new_stock)
        product.save()
        msg = '!!!!!!!!!!!!!!! stock updated !!!!!!!!!!!!'
        

    return render(request, 'sellerpage/update_stock.html', {'data_stock': product_stock, 'data': seller_data,'msg':msg})

@auth_seller
def log_out(request):
    del request.session['seller']
    request.session.flush()  # to remove session from django_session table
    return redirect('common:prohome')

@auth_seller
def proff(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'sellerpage/profile.html', {'data': seller_data})

@auth_seller
def get_stock(request):
    id = request.POST['id']
    product = Product.objects.get(id=id)
    product_name = product.product_name
    current_stock = product.product_stock
    p_id = product.id
    return JsonResponse({'pro_name': product_name, 'stock': current_stock, 'pr_id': p_id})

