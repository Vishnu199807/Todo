from django.shortcuts import render,redirect
from django.views.generic import View
from Todo import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=forms.RegistrationFrom()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = forms.RegistrationFrom(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"registration.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("login success")
                return render(request,"loin.html",{"form":form})

            else:
                print("invalid credentials")
                return render(request,"login.html",{"form":form})

        return render(request,"login.html")
class Indexview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return  redirect(("signin"))

