# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View
from users.forms import LoginForm,RegisterForm
from .models import UserProfile,EmailVerifyRecord
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_register_email
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username","")
            pass_word = request.POST.get("password","")
            user = authenticate(username=user_name,password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,"index.html")
                else:
                    return render(request, "login.html", {"msg": "error"})
            else:
                return render(request,"login.html",{"msg":"error"})
        else:
            return render(request, "login.html", {'login_form': login_form})

class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        return render(request,"login.html")



class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,"register.html",{'register_form': register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username","")
            user_email = request.POST.get("email","")
            pass_word = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_email
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_email,"register")
            return render(request,"login.html")
        else:
            return render(request,"register.html")

