from django.shortcuts import render,redirect
from datetime import datetime
from .models import customer
from django.contrib import messages
# for mail
from django.core.mail import send_mail,EmailMessage#for file send in the mail
from django.template.loader import render_to_string

#for authentiaction
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
#for login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='log_in')
def index(request):
    date=datetime.now()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phone']
        msg=request.POST['message']
        data=customer(name=name,email=email,phone=phno,message=msg)
        data.save()
        subject='thanks for visiting EVEREST MOMOS'
        message=render_to_string('main/mailformat.html',{'name':name,'date':date})
        from_email='ashishrajpoudel28@gmail.com'
        recipient_list=[email]
        variable=EmailMessage(subject,message,from_email,recipient_list)
        variable.send(fail_silently=True)
        messages.success(request,f"Hi {name} your response is sucessfully submit please check your mail!!")
        
    
    return render(request,'main/index.html',{'date':date})
def about(request):
    return render(request,'main/about.html')
def menu(request):
    return render(request,'main/menu.html')
@login_required(login_url='log_in')
def contact(request):
    return render(request,'main/contact.html')
def services(request):
    return render(request,'main/services.html')


"""
_______________________authetication___________________
"""
def Register(request):
 
    if request.method =='POST': 
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirmpassword')
        try:
            if uname.lower() in password.lower():
                messages.error(request,"username and password is too similar!!")
                return redirect('register')
            if not re.search(r"[A-Z]",password):
                messages.error(request,'your password contain at least one Capital letter')
            if not re.search(r"\d",password):
                messages.error(request,'your password contain at least one Digit')
            validate_password(password)
            if password == cpassword:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,'username already exist')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email already exist')
                    return redirect('register')
                else:
                    User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
                    messages.success(request,'data submitted sucessfully!!')
                    return redirect('register')
            
            else:
                messages.error(request,'password and confirm password doesnot match')
                return redirect('register')
        except ValidationError as e:
            for error in e.messages:
                messages.error(request,error)
            return redirect('register')
        
    return render(request,'auth/register.html')


def log_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username):
            messages.info(request,'invalid credential!!')
            return redirect('log_in')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'auth/login.html')

def log_out(request):
    logout(request)
    return redirect("log_in")