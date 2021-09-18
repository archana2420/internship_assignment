from django import forms
from django.forms import ModelForm
from.models import User_info




class Sign_up_Form(ModelForm,forms.Form):
    class Meta:
        model=User_info
        fields=['username','email','password','address']
    confirm_password = forms.CharField()

class loginForm(forms.Form):
    email=forms.EmailField(max_length=32)
    password=forms.CharField(max_length=32,widget=forms.PasswordInput)
