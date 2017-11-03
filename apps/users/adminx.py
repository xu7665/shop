# _*_ coding:utf-8 _*_
from .models import Acritcle
import xadmin

class AcritcleAdmin(object):
    list_display = ('user','title','content_desc','add_time')

xadmin.site.register(Acritcle,AcritcleAdmin)
