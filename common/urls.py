from django.urls import path

from . import views

app_name = 'common'
urlpatterns=[
    path('pjt_home',views.p_home,name='prohome'),
    path('cust_login',views.c_home,name='cuslog'),
    path('c_signup',views.c_signup,name='custsp'),
    path('seller_login',views.s_home,name='seller'),
    path('seller_signin',views.s_signin,name='sellersu'),
    path('exist_email',views.email_exist,name='check_email'),
    

]