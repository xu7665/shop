# _*_ coding:utf-8 _*_
from .models import Acritcle,EmailVerifyRecord,UserProfile
from xadmin.plugins.auth import UserAdmin
import xadmin
from xadmin import views
from django.contrib.auth.models import User

class UserProfileAdmin(UserAdmin):
    pass

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "Vincent--Blog"
    site_footer = "旭空间"
    menu_style = "accordion"


class AcritcleAdmin(object):
    list_display = ('user','title','content_desc','add_time','content_text')
    search_fields = ('user','title','content_desc','add_time','content_text')
    list_filter = ('user','title','content_desc','add_time','content_text')
    style_fields = {"content_desc":"ueditor"}

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type',]
    list_filter = ['code','email','send_type','send_time']

# class UserProfileAdmin(object):
#     list_display = ('name','birthday','gender','mobile','mages','email')
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Acritcle,AcritcleAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)