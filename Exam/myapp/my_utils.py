from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
import uuid
import hashlib

# 获取随机字符串
def get_random_str():
    # 获得uuid值
    uuid_val = uuid.uuid4()
    # 将uuid值转成字符串
    uuid_str = str(uuid_val).encode("utf-8")
    # 获得md5实例
    md5 = hashlib.md5()
    # 将uuid字符串做摘要
    md5.update(uuid_str)
    # 返回固定长度的字符串
    return md5.hexdigest()

import random
def get_random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)

def get_token():
    uuid_str = str(uuid.uuid4()).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

def send_active_email(email):
    token = get_token()
    cache.set(token, email, 60*10)
    from_email = "215480518@qq.com"
    to = [email]
    subject = "激活邮件"
    confirm_url = "http://10.3.133.81:12000/Myapp/active/" + token
    content = "将以下激活连接复制到浏览器" + confirm_url
    send_mail(subject, content, from_email, to)