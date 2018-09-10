import os
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from PIL import Image, ImageDraw, ImageFont

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from .models import MyUser
from .my_utils import get_random_str, get_random_color

import io
import random
USER_PEER_PAGE_NUM = 4


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        params = request.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')
        phone = params.get('phone')
        email = params.get('email')
        if u_name and len(u_name)>2 and phone and len(phone)>3 and  pwd and confirm_pwd and len(pwd)>2 and pwd==confirm_pwd:
            # 判断是否被注册

            exists_flag = MyUser.objects.filter(username=u_name).exists()
            if exists_flag:
                return HttpResponse('用户名不可用')
            else:
                MyUser.objects.create_user(username=u_name, password=pwd, email=email)
                return redirect('/myapp/login')
        else:
            return HttpResponse('用户名不可用')

def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        params = request.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        user = authenticate(username=u_name, password=pwd)
        print(user)
        if user:
            login(request, user)
            print(user)
            return redirect('/myapp/index')
        else:
            return HttpResponse('错误')

@login_required(login_url="/myapp/login")
def index(req):
    # 拿用户
    user = req.MyUser
    return render(req, 'index.html', {'u_name': user.username})

def get_user_by_num(request, page_num):
    # 获取全部用户
    users = MyUser.objects.all()
    # 创建分页
    paginator = Paginator(
        users,
        USER_PEER_PAGE_NUM,
    )
    # 参数校验
    if int(page_num)<1 or int(page_num)>paginator.num_pages:
        return HttpResponse('没数据了')
    # 拿到用户指定页码的数据
    page = paginator.page(page_num)
    # 返还数据
    data = {
        'users': page.object_list
    }
    return render(request, 'paginator.html', data)
    pass

@login_required(login_url='/myapp/login')
def update_msg(request):
    user = request.user
    if request.method == "GET":
        data = {
            'u_name': user.username,
            'icon': '/static/uploads/' + user.icon.url
        }
        return render(request, 'person.html', data)
    else:
        # （自带的）
        # # 拿文件
        # icon = request.FILES['u_icon']
        # # 保持头像
        # user.icon =icon
        # user.save()

        # 原生
        # 拿文件数据
        icon = request.FILES['u_icon']
        file_name = 'icons/' + get_random_str() + '.jpg'
        # 拼接一个自己的文件路径
        image_path = os.path.join(settings.MEDIA_ROOT, file_name)
        # 打开拼接的文件路径
        with open(image_path, 'wb') as fp:
            # 遍历图片文件的块数据
            for i in icon.chunks():
                # 将图片数据写入文件
                fp.write(i)

        # 拼接返回数据
        data = {
            'u_name': MyUser.username,
            'icon': '/static/uploads/' + file_name
        }
        print(user.icon)
        return render(request, 'person.html', data)

def get_verify_img(request):
    # 画布背景颜色
    bg_color = (120, 120, 0)
    img_size = (150,70)
    # 实例化一个画布
    image = Image.new('RGB',img_size , bg_color)
    # 实例化画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 设置文字颜色
    # text_color = (255,0,0)
    # 创建字体
    font_path = '/home/tan/gz1803/day07/static/fonts/ADOBEARABIC-BOLD.OTF'
    font = ImageFont.truetype(font_path, 30)
    source = 'abcdefGsjfjfljflwjJLJLJLJFJJFIJFUIURWRUUQWETIOA'
    # 保存随机的字符
    code_str = ''
    for i in range(4):
        tmp_num = random.randrange(len(source))
        random_str = source[tmp_num]
        code_str += random_str
        text_color = get_random_color()

        draw.text((10+i*30, 20), random_str, text_color, font)
    # 记录给哪个请求发了什么验证码
    request.session['code'] = code_str
    # 使用画笔将文字画到画布
    # draw.text((10, 20), "2", text_color, font)
    # draw.text((40, 20), "3", text_color, font)
    # draw.text((70, 20), "2", text_color, font)
    # 获得一个缓存区

    buf =io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回到前端
    return HttpResponse(buf.getvalue(), 'image/png')

def mylogin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        params = request.POST
        # 用户输入的
        code = params.get('verify_code')
        server_code = request.session.get('code')
        print(server_code)
        if server_code.lower() == code.lower():
            print('1')
            return HttpResponse('ok')
        else:
            print('2')
            return HttpResponse('..')