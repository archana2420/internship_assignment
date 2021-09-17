from django.shortcuts import render
from django.http import HttpResponse
from .form import Sign_up_Form
# Create your views here.


def login_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sign_up_page(request):
    form=Sign_up_Form()
    if request.method=="post":
        if form.is_valid():
            pass 
    else:
        return render(request,'sign_up.html',{'form':form})