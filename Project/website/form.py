from django import forms
from django.forms import ModelForm
from.models import User_info
class Sign_up_Form(forms.Form):
    username=forms.CharField(max_length=15)
    email=forms.EmailField(max_length=32)
    password=forms.CharField(max_length=32)
    confirm_password=forms.CharField()
    address=forms.CharField()

class Sign_up(ModelForm,forms.Form):
    class Meta:
        model=User_info
        fields=['username','email','password','address']
    confirm_password = forms.CharField()