# _*_ coding:utf-8 _*_
from .models import Acritcle,UserProfile
from xadmin.plugins.auth import UserAdmin
import xadmin

class AcritcleAdmin(object):
    list_display = ('user','title','content_desc','add_time')

class UserProfileAdmin(object):
    list_display = ('name','birthday','gender','mobile','mages','email')

xadmin.site.unregister(UserProfile)
xadmin.site.register(Acritcle,AcritcleAdmin)
xadmin.site.register(UserProfile,UserProfileAdmin)