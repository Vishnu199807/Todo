from django import forms
from django.contrib.auth.models import User


#class RegistrationFrom(forms.Form):
    #first_name=forms.CharField()
    #last_name=forms.CharField()
    #user_name=forms.CharField()
    #email=forms.EmailField()
   ## password=forms.CharField()

class RegistrationFrom(forms.ModelForm):
  class Meta:
      model=User
      fields=["first_name","last_name","username","email","password"]
      widgets={
          "password":forms.PasswordInput(attrs={"class":"form-control"}),
          "email":forms.EmailInput(attrs={"class":"form-control"}),
          "first_name":forms.TextInput(attrs={"class":"form-control"}),
          "last_name":forms.TextInput(attrs={"class":"form-control"}),
          "username":forms.TextInput(attrs={"class":"form-control"}),
       }

class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

