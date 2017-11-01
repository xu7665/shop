from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from Shop.settings import DEFAULT_FROM_EMAIL
def send_register_email(email,send_type="register"):
    email_recode = EmailVerifyRecord()
    code = random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    if send_type == "register":
        email_title = "激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title,email_body,DEFAULT_FROM_EMAIL,[email])
        if send_status:
            pass
def random_str(randomlength=8):
    srt = ''
    chars = 'AaBbCcDdKNLDASMslkadmlkmLALMDlldmlMliIQOiyyTtycXxF77900643134567098'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        srt+=chars[random.randint(0,length)]
    return srt




def generrate_random_str():
    pass
