from django.urls import path
from .import views

app_name='customer'
urlpatterns=[
    path('c_home',views.cust_home,name='customer_home'),
    path('profile',views.my_profile,name='myprofile'),
    path('list',views.cat,name='cat_l'),
    path('logout',views.log_out,name='logout_cust'),
    path('ch_pass',views.changepass_cust,name='c_custpass'),
    path('p_detail/<int:pid>',views.product_detail,name='pro_details'),
    path('mycart',views.my_cart,name='cart'),
    path('order',views.my_order,name='myorder'),
    path('remove_cart/<int:pid>',views.remove_item,name='remove_cart'),
    path('master',views.master,name='master'),
    path('purchase/<int:pid>',views.purchase,name='purchase')
    

]