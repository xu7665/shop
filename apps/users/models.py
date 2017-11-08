# _*_ coding:utf-8 _*_
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField
# Create your models here.
class UserProfile(AbstractUser):
    '''
    用户
    '''
    GENDER = (
        ("male","男"),
        ("female","女"),
    )

    name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    birthday = models.DateField(null=True,blank=True,verbose_name="出生年月")
    gender = models.CharField(max_length=6,choices=GENDER,default="female",verbose_name="性别")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.name)

class VerifyCode(models.Model):
    code = models.CharField(max_length=50,verbose_name="验证码")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.code


class EmailVerifyRecord(models.Model):
    EMAIL_TYPE = (
        ("register","注册"),
        ("forget","忘记密码" ),
    )

    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(max_length=10,choices=EMAIL_TYPE,default="register", verbose_name=u"验证码类型")
    send_time = models.DateTimeField(verbose_name=u"发送时间",default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)

class Acritcle(models.Model):
    user = models.ForeignKey(UserProfile,null=True,blank=True,verbose_name="作者")
    title = models.CharField(max_length=15,verbose_name="标题")
    content_desc = UEditorField(verbose_name=u'内容',imagePath="users/images/",width=1000,height=300,filePath="users/files/",default='')
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user