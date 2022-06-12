from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RegistrationForm

import random
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


otp=random.randint(100000,999999)

def RegisterView(request):
    form = RegistrationForm()
    template_name = 'auth_App/register.html'
    context = {'form':form}
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request,template_name,context)

def LoginView(request):
    template_name='auth_app/login.html'
    if request.method=='POST':
        un=request.POST.get('u')
        pw=request.POST.get('p')
        global user
        user=authenticate(username=un,password=pw)
        subject = 'welcome to Laptop world'
        message = f'Hi {user.username}, your OTP for login is {otp}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list ) 
        return redirect('otp_url')
    context={}
    return render(request,template_name,context)

def OtpView(request):
    template_name='auth_app/otp.html'
    context={}
  
    if request.method=='POST':
        if user is not None:
            print(request.POST.get('otp_u'))
            
            otp_user=int(request.POST.get('otp_u'))
            print(type(request.POST.get('otp_u')))
            if otp==otp_user:
                login(request,user)
                return redirect('showlap_url')
    return render(request,template_name,context)

def LogoutView(request):
    logout(request)
    return redirect('login_url')