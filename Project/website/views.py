from django.shortcuts import render
from django.http import HttpResponse
from .form import Sign_up_Form,Sign_up
from .models import User_info

# Create your views here.


def login_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sign_up_page(request):
    form=Sign_up()
    if request.method=="POST":
        print("post")
        if form.is_valid():
            username=request.POST['username']
            email= request.POST['email']
            password=request.POST['password']
            address=request.POST['address']
            print(username)
            info=User_info(username=username,email=email,password=password,address=address)
            info.save()
            return render(request,'login.html')
    else:
        return render(request,'sign_up.html',{'form':form})