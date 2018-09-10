from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MyUser, Person
from .my_utils import get_random_str, send_active_email
from django.core.mail import send_mail
import os
# Create your views here.

def register(req):
    if req.method == 'GET':
        return render(req, 'register.html')
    else:
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')
        email = params.get('email')
        icon = req.FILES['u_icon']
        if u_name and pwd and confirm_pwd and email  and pwd==confirm_pwd and len(u_name)>3 and len(pwd)>3:
            exists_flag =MyUser.objects.filter(username=u_name).exists()
            if exists_flag:
                return HttpResponse('用户名已存在')
            else:
                user = MyUser.objects.create_user(username=u_name, password=pwd, email=email, is_active=False)
                # 拿文件数据
                # icon = req.FILES['u_icon']
                # 生成随机文件名字
                file_name = "icons/" + get_random_str() + ".jpg"
                # print(file_name)
                user.icon = file_name
                # print(user)
                user.save()
                # 拼接一个自己的文件路径
                image_path = os.path.join(settings.MEDIA_ROOT, file_name)

                # 打开你拼接的那个文件路径
                with open(image_path, 'wb') as fp:
                    # 遍历图片文件的块数据
                    for i in icon.chunks():
                        # 将图片数据 写入到我们自己的那个文件
                        fp.write(i)
                # data = {
                #     'u_name': user.username,
                #     'icon': "/static/uploads/" + file_name
                #
                # }
                new_email = user.email
                send_active_email(new_email)
                # title = '没有标题'
                # msg = '异步'
                # from_email = settings.DEFAULT_FROM_EMAIL
                # print(user.email)
                # new_email = user.email
                # recievers = [new_email, ]
                # send_mail(
                #     title,
                #     msg,
                #     from_email,
                #     recievers,
                #     fail_silently=True
                # )
                return redirect(reverse('myapp:login'))

        return HttpResponse('填写错误')

# 激活
def active(req, token):
    email = cache.get(token)
    if email:
        user = MyUser.objects.filter(email=email)
        if user.count() == 1:
            MyUser.objects.filter(email=email).update(is_active=True)
            return redirect(reverse('myapp:login'))
        else:
            return HttpResponse("<h1>密码失效</h1>")
    else:
        return HttpResponse("<h1>密码失效</h1>")


def my_login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        if u_name and pwd and len(u_name)>3 and len(pwd)>3:
            # 用户校验
            user = authenticate(username=u_name, password=pwd)
            # print(dir(user), user)
            if user:
                act = MyUser.objects.filter(username=u_name)[0].is_active
                print(act)
                if act:
                    login(req, user)
                    return redirect(reverse('myapp:index'))
                else:
                    return HttpResponse('用户未激活')
            return HttpResponse('用户名或密码错误')
        return HttpResponse('填写错误')
        pass

    pass

def index(req):
    if req.method == 'GET':
        user = req.user
        person = Person.objects.all()
        data = {
            'username' : user.username,
            'is_login': False,
            'person' : person
        }
        return render(req, 'home_logined.html', data)
    else:
        print('1')
        # if user:
        data = {
            # 'username' : user.username,
            'is_login' : False,
        }
        return render(req, 'home_logined.html', data)
        pass

def inf(req):
    return HttpResponse('ok')