from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.models import User
from restaurantapp.models import feedback, newregister, newregister1,newregister2,feedback
from datetime import datetime
from django.contrib import messages

# Create your views here.
def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # print(u password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'your username or password doesn"t match',extra_tags='loginpage')
            return render(request,'loginpage.html')
    else:
        return render(request,'loginpage.html')

def homepage(request):
    if request.user.is_anonymous:
      return redirect('/loginpage')
        
    else:
        return render(request,'homepage.html')
def logoutpage(request):
    logout(request)
    return redirect('/loginpage')

def register(request):
    if request.method=='POST':  
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
          if User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken',extra_tags='register')
            return redirect('register')
          else:
                new_register=User.objects.create_user(username,email,password1)
                new_register.first_name=firstname
                new_register.last_name=lastname
                new_register.save()
                messages.success(request,'You have successfully registered ',extra_tags='loginpage')
                return redirect('loginpage')
                
        else:
            messages.info(request,'Your password is not matching',extra_tags='register')
            return redirect('register')
    else: 
        
        return render(request,'register.html')

def response(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        textarea=request.POST['textarea']
        user=feedback(fullname=fullname,email=email,textarea=textarea,date=datetime.today())
        user.save()
        messages.success(request,'Thank you for your feedback ',extra_tags='response')
        return redirect('homepage')
    else:
        return redirect('homepage')