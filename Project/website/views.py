from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Sign_up_Form,loginForm
from .models import User_info



# Create your views here.




def sign_up_page(request):
    form=Sign_up_Form
    if request.method=="POST":
        form=Sign_up_Form(request.POST)
        print("post")
        if form.is_valid():
            print("form valid func")
            username=request.POST['username']
            email= request.POST['email']
            password=request.POST['password']
            address=request.POST['address']
            print(username)
            info=User_info(username=username,email=email,password=password,address=address)
            info.save()

            return redirect('login_page')
    else:
        return render(request,'sign_up.html',{'form':form})

def login_page(request):
    form=loginForm()

    if request.method=="POST":
        form=loginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = User_info.objects.filter_by(email=email).first()
            verify = True if (user.password == password) else False
            if user and verify :
                return redirect('display_info')


    return render(request,'login.html',{'form':form})

def display_info(request):
    all_entries=User_info.objects.all()
    return render(request, 'display_info.html', {'entries':all_entries})