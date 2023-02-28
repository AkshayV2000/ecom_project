from django.urls import path
from .import views

app_name='sellerpage'

urlpatterns=[
    path('sellerhome',views.sl_h,name='sellerhome'),
    path('products',views.add_pro,name='addproduct'),
    path('catalog',views.cato_log,name='productcatolog'),
    path('changepassword',views.change_pass,name='c_password'),
    path('history',views.od_history,name='o_history'),
    path('recent',views.r_history,name='recent_history'),
    path('update',views.s_update,name='update_stock'),
    path('logout',views.log_out,name='logout_cust'),
    path('sell_profile',views.proff,name='profile'),
    path('get_stock',views.get_stock,name='up_stock'),
    
]