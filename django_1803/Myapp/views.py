import io

import random

import os
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MyUser
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse

from .my_utils import get_random_str, get_random_color


# Create your views here.

# 图片验证码
def verify_img(req):
    # 画布背景颜色
    bg_color = get_random_color()
    img_size = (130, 70)
    # 实例化一个画布
    image = Image.new("RGB", img_size, bg_color)
    # 实例化画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 设置文字的颜色
    # text_color = (255, 0, 0)
    # 创建字体
    font_path = "/home/tan/gz1803/django_1803/static/fonts/ADOBEARABIC-BOLDITALIC.OTF"
    font = ImageFont.truetype(font_path, 30)
    source = "abcdefghijklmnopqrstJHHKJLHKHATQWERTYUIOPXCVBNMDFGHJKL1234567890"

    # 保存每次随出来的字符
    code_str = ""
    for i in range(4):
        text_color = get_random_color()
        # 获得随机数字
        tmp_num = random.randrange(len(source))
        # 获得随机字符
        random_str = source[tmp_num]
        code_str += random_str
        draw.text((10 + 30*i, 20), random_str, text_color, font)

    # 记录给哪个请求发了什么验证码
    req.session['code'] = code_str

    # 使用画笔将文字画到画布上
    # draw.text((10, 20), "X", text_color, font)
    # draw.text((40, 20), "z", text_color, font)
    # draw.text((60, 20), "9", text_color, font)

    # 获得一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容 返回给前端
    return HttpResponse(buf.getvalue(), 'image/png')

def test(req):
    return render(req,'test.html')


def my_login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        verify_code = params.get('verify_code')
        # 数据校验
        if u_name and pwd and len(u_name)>2 and len(pwd)>2:
            user = authenticate(username=u_name, password=pwd)
            if user :
                print(req.session['code'])
                if verify_code.lower() != req.session['code'].lower():
                    return HttpResponse('验证码错误')
                else:
                    login(req, user)
                    # return redirect(reverse('Myapp:index', {'u_name': user.username}))
                    # return render(req, 'index.html', context={'u_name': user.username})
                    # return redirect('/Myapp/index')
                    return redirect(reverse('Myapp:index'))
            else:
                return HttpResponse('失败')
        else:
            return HttpResponse('用户名或密码太短')

def register(req):
    if req.method == 'GET':
        return render(req, 'register.html')
    else:
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')
        u_email = params.get('u_email')
        u_phone = params.get('u_phone')
        if u_name and pwd and confirm_pwd and pwd == confirm_pwd and len(u_name)>2 and len(pwd)>2:
            exists_flag_one = MyUser.objects.filter(username=u_name).exists()
            exists_flag_two = MyUser.objects.filter(phone=u_phone).exists()
            if exists_flag_one:
                return HttpResponse('用户已存在')
            elif exists_flag_two:
                return HttpResponse('电话号码已注册')
            else:
                user = MyUser.objects.create_user(username=u_name, password=pwd,
                                                  email=u_email, phone=u_phone)
                return redirect(reverse('Myapp:login'))
        return HttpResponse('用户名或密码错误')

    pass

@login_required(login_url='/Myapp/login')
def upload(req):
    user = req.user
    if req.method == 'GET':
        data = {
            'u_name': user.username,
            'icon': "/static/uploads/" + user.icon.url
        }
        # print(user.icon.url)
        return render(req, 'upload.html', data)
    else:
        # # 拿文件
        # icon = req.FILES['u_icon']
        # # 保存头像
        # user.icon = icon
        # print(user)
        # user.save()
        # # 拼接返回数据

        # 原生
        # 拿文件数据
        icon = req.FILES['u_icon']
        print(icon)
        # print(icon.name)

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
        data = {
            'u_name': user.username,
            'icon': "/static/uploads/" + file_name

        }
        print(dir(user.icon))
        return render(req, 'index.html', data)

    pass

# @login_required(login_url='/Myapp/login')
def index(req):
    user = req.user
    print(user)
    if req.method == 'GET':
        print('1')
        if str(user) == 'AnonymousUser':
            print('2')
            data = {
                'u_name': user.username,
                'icon': "/static/img/def.jpg"
            }
        else:
            print('3')
            try:
                new_icon = "/static/uploads/" + user.icon.url
                data = {
                    'u_name': user.username,
                    'icon': new_icon
                }
            except:
                data = {
                    'u_name': user.username,
                    'icon': "/static/img/def.jpg"

                }
        return render(req, 'index.html', data)
    else:
        data = {
            'u_name': user.username,
            'icon': "/static/uploads/" + user.icon.url

        }
        return render(req, 'index.html', data)

def my_logout(req):
    logout(req)
    return redirect('/Myapp/index')