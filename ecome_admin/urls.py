from django.urls import path
from .import views

app_name='ecom_admin'
urlpatterns=[
    path('ecomadmin_home',views.ecomadmin_home,name='ecomadminhome'),
    path('approve_cust',views.approve_cust,name='approvecust'),
    path('approve_seller',views.approve_seller,name='approveseller'),
    path('view_cust',views.view_cust,name='viewcust'),
    path('view_seller',views.view_seller,name='viewseller'),
    path('approve/<int:sid>',views.approve,name='approve'),
    path('deletesell/<int:sid>',views.delete_seller,name='delete_seller'),   
    path('deletecust/<int:sid>',views.delete_cust,name='delete_cust'),    
]