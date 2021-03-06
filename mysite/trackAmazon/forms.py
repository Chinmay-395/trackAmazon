from django import forms
from .models import *


class UrlForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter product link like https://www.amazon.in/Apple-iPhone-5s-Gold-16GB/dp/B00FXLCD38'}))

    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

#
# class EmailForm(forms.Form):
#     email_id = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
#     price = forms.CharField(widget=forms.TextInput(attrs={'claass':'form-control','placeholder':'Enter Price'}))

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']