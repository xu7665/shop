# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View
from users.forms import LoginForm,RegisterForm
from django.http import HttpResponse
from .models import UserProfile,EmailVerifyRecord,Acritcle,Comments
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_register_email
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
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
                active_email = record.email
                active_user = UserProfile.objects.get(email=active_email)
                active_user.is_active = True
                active_user.save()
            else:
                return render(request,"active_faild.html")
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
            if UserProfile.objects.filter(email=user_email):
                return render(request, "register.html")
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

class Index_login(View):
    def get(self,request):
        all_acritcl = Acritcle.objects.all()
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_acritcl,5,request=request)
        acritcl = p.page(page)
        return render(request, "index.html", {"all_acritcl": acritcl})

class Org_list(View):
    def get(self,request,id):
        all_org = Acritcle.objects.all().filter(id=id)
        return render(request,"org-list.html",{"all_org":all_org})

def page_not_found(request):
    response = render_to_response('404.html',{})
    response.status_code = 404
    return response

class CommentsView(View):
    def get(self,request,id):
        course = Acritcle.objects.get(id=int(id))
        all_comments = Comments.objects.all()
        return render(request,"",{"course":course,"all_comments":all_comments})




class AddCommentsView(View):
    def post(self,request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')
        # course_id = request.POST.get("id",0)
        comments = request.POST.get("comments","")
        if comments:
            course_comments = Comments()
            # couese = Acritcle.objects.get(id=int(course_id))
            # course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"评论成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"评论失败"}', content_type='application/json')
            # all_article = Acritcle.objects.get(id=int(id))
            # all_comments = Comments.objects.all()
            # return render(request,"commnet.html",{
            #     "all_article":all_article,
            #     "all_comments":all_comments
            # })



# def index_login(request):
#     all_acritcl = Acritcle.objects.all()
#     return render(request,"index.html",{"all_acritcl":all_acritcl})