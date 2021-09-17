from django import forms

class Sign_up_Form(forms.Form):
    username=forms.CharField(max_length=15)
    email=forms.EmailField(max_length=32)
    password=forms.CharField(max_length=32)
    confirm_password=forms.CharField()
    address=forms.CharField()

