from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.urls import reverse
from django.views.decorators.cache import cache_page
from .models import MyUser

# from .models import Player
from .my_util import get_random_color
import io
import random
import time


# Create your views here.
def verify_img(request):
    # 画布背景颜色
    bg_color = get_random_color()
    # 图片大小
    width = 130
    height = 50
    # 实例化一个画布
    image = Image.new('RGB', (width, height), bg_color)
    # 实例化画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 设置文字颜色
    # text_color = (255,0,0)
    # 创建字体
    font_path = '/home/tan/gz1803/day07/static/fonts/ADOBEARABIC-BOLD.OTF'
    font = ImageFont.truetype(font_path, 30)
    source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    # 保存随机的字符
    code_str = ''
    for i in range(4):
        tmp_num = random.randrange(len(source))
        random_str = source[tmp_num]
        code_str += random_str
        text_color = get_random_color()

        draw.text((10 + i * 30, 20), random_str, text_color, font)
    # 记录给哪个请求发了什么验证码
    request.session['code'] = code_str
    # 使用画笔将文字画到画布
    # draw.text((10, 20), "2", text_color, font)
    # draw.text((40, 20), "3", text_color, font)
    # draw.text((70, 20), "2", text_color, font)
    # 划几根干扰线
    for num in range(4):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

        # 模糊下,加个帅帅的滤镜～
    im = image.filter(ImageFilter.FIND_EDGES)
    # 获得一个缓存区

    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回到前端
    return HttpResponse(buf.getvalue(), 'image/png')


def register(req):
    if req.method == 'GET':
        return render(req, 'supermarket/register.html')
    else:
        params = req.POST
        u_name = params.get('username')
        pwd = params.get('passwd')
        confirm_pwd = params.get('confirm_pwd')
        u_email = params.get('u_email')
        u_phone = params.get('u_phone')
        verify_code = params.get('verify_code')
        print(u_name, pwd, confirm_pwd)
        if u_name and pwd and confirm_pwd and pwd == confirm_pwd and len(u_name) > 2 and len(pwd) > 2:

            if verify_code.lower() != req.session['code'].lower():
                return HttpResponse('验证码错误')
            else:
                exists_flag_one = MyUser.objects.filter(username=u_name).exists()
                exists_flag_two = MyUser.objects.filter(phone=u_phone).exists()
                if exists_flag_one:
                    return HttpResponse('用户已存在')
                elif exists_flag_two:
                    return HttpResponse('电话号码已注册')
                else:
                    user = MyUser.objects.create_user(username=u_name, password=pwd,
                                                      email=u_email, phone=u_phone)
                    return redirect(reverse('supermarket:mylogin'))
        return HttpResponse('用户名或密码错误')


def mylogin(req):
    if req.method == 'GET':
        return render(req, 'supermarket/login.html')
    else:
        params = req.POST
        u_name = params.get('username')
        pwd = params.get('passwd')
        verify_code = params.get('verify_code')
        # 数据校验
        if u_name and pwd and len(u_name) > 2 and len(pwd) > 2:
            user = authenticate(username=u_name, password=pwd)
            if user:
                if verify_code.lower() != req.session['code'].lower():
                    return HttpResponse('验证码错误')
                else:
                    login(req, user)
                    print('11')
                    return redirect(reverse('supermarket:index'))
            else:
                return HttpResponse('用户名或密码错误')
        else:
            return HttpResponse('用户名或密码太短')


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
        return render(req, 'supermarket/index.html', data)
    else:
        data = {
            'u_name': user.username,
            'icon': "/static/uploads/" + user.icon.url

        }
        return render(req, 'supermarket/index.html', data)
