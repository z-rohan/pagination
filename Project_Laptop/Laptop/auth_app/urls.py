from django.urls import path 
from .views import *

urlpatterns=[
    path('reg/',RegisterView,name='register_url'),
    path('li/',LoginView,name='login_url'),
    path('lo/',LogoutView,name='logout_url'),
    path('otp/',OtpView,name='otp_url')
]