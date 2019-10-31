from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model=UserProfileInfo
         fields=('portfolio_site','profile_pic')

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())#this column parameter is to provide extra validators to password column already defined in User class.

    class Meta():
        model=User
        fields=('username','email','password')
