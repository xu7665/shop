from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View
from users.forms import LoginForm,RegisterForm
from .models import UserProfile
from django.contrib.auth.hashers import make_password
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
                login(request,user)
                return render(request,"index.html")
            else:
                return render(request,"login.html",{"msg":"用户名或密码出错"})
        else:
            return render(request, "login.html", {'login_form': login_form})

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,"register.html",{'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username","")
            pass_word = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()

