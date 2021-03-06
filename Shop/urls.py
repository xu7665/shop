"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,Index_login,Org_list
from users.views import AddCommentsView
from django.views.static import serve
from .settings import MEDIA_ROOT
from users.views import page_not_found
import xadmin
import Shop.settings
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
#    url('^index/$',TemplateView.as_view(template_name="index.html"),name="index"),
    url('^index/$',Index_login.as_view(),name="index"),
    url('login/$',LoginView.as_view(),name='login'),
    url('^register/$',RegisterView.as_view(),name="register"),
    url('^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    url(r'^add_comment/$',AddCommentsView.as_view(),name="add_comments"),
    url(r'^post/(?P<id>.*)/$',Org_list.as_view(),name="psot"),
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT})
]

handler404 = 'users.views.page_not_found'