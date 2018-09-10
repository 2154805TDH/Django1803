from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.template import loader
from .my_utils import get_random_str
# Create your views here.

def send_my_email(request):
    title = '阿里offer'
    msg = '恭喜你获得海天蚝油一瓶'

    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3043433960@qq.com',
        '1511128449@qq.com',
    ]
    send_mail(title, msg, email_from, reciever)
    return HttpResponse('ok')

def send_email_v1(request):
    title = '阿里offer'
    msg = ''

    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3043433960@qq.com',
        '1511128449@qq.com',
    ]
    # 加载模板
    template = loader.get_template('email.html')
    # 渲染模板
    html_str = template.render({'msg':'双击666'})
    send_mail(title, msg, email_from, reciever, html_message=html_str)
    return HttpResponse('ok')

def verify(request):
    if request.method == 'GET':
        return render(request, 'verify.html')
    else:
        params = request.POST
        email = params.get('email')
        # 生成随机字符
        random_str = get_random_str()
        # 拼接验证链接
        url = 'http://10.3.50.49:12000/myapp/active/' + random_str
        # 加载激活模板
        tmp = loader.get_template('active.html')
        html_str = tmp.render({'url':url})
        title = '阿里offer'
        msg = ''

        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            email,
        ]
        cache.set(random_str, email, 120)
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        return HttpResponse('ok')

def active(req, random_str):
    res = cache.get(random_str)
    if res:
        # 通过邮箱找到对应用户
        # 更新用户的激活状态
        return HttpResponse(res+'激活成功')
    else:
        return HttpResponse('验证失败')

def send_many_email(request):
    title = '阿里offer'
    content1 = '恭喜你获得海天蚝油一瓶'

    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3043433960@qq.com',
        '1511128449@qq.com',
    ]
    # 邮件1
    msg1 = (title, content1, email_from, reciever)
    # 邮件2
    msg2 = ('早生贵子', content1, email_from, ['1511128449@qq.com'])
    send_mass_mail((msg1, msg2), fail_silently=True)
    return HttpResponse('ok!')
