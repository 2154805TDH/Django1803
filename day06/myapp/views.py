import os
from django.conf import settings

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MyUser
from .my_utils import get_random_str
# Create your views here.
USER_PEER_PAGE_NUM = 4

def test(req):
    return render(req,'test.html')



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        params = request.POST
        u_name = params.get('u_name')
        phone = params.get('phone')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')
        email = params.get('email')
        if u_name and len(u_name)>2 and phone and len(phone)>3 and  pwd and confirm_pwd and len(pwd)>2 and pwd==confirm_pwd:
            # 判断是否被注册

            exists_flag = MyUser.objects.filter(username=u_name).exists()
            if exists_flag:
                return HttpResponse('用户名不可用')
            else:
                MyUser.objects.create_user(username=u_name, password=pwd, email=email, phone=phone)
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
    user = req.user
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
        # print(file_name)
        # 保存
        user.icon = file_name
        # print(user)
        user.save()
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
            'u_name': user.username,
            'icon': '/static/uploads/' + file_name
        }
        print(user.icon)
        return render(request, 'person.html', data)
