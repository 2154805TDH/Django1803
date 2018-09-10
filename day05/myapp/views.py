from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse

# Create your views here.
from django.urls import reverse

from .models import MyUser


def index(req):
    print(req)
    print(dir(req))
    return HttpResponse('ok')

def response_index(req):
    respose = HttpResponse()
    respose.content = '我是content设置的'
    # 追加
    respose.write('我是write写的')
    # 覆盖
    respose.content = '我是content设置的'
    respose.flush()
    respose.status_code = 404
    return respose

def get_josn(req):
    data = [1,2,3]
    return JsonResponse({'data':data})

def get_2048(req):
    return render(req,'2048.html')

def my_login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        name = params.get('u_name')
        # 校验
        response = HttpResponse()
        # 设置cookie
        response.set_cookie('u_name',name, max_age=5)
        # 设置session
        req.session['ll'] = 'name'
        response.content = '登录成功'
        return response

def my_index(req):
    u_name = req.COOKIES.get('u_name')
    name = req.session.get('ll')
    print(name)
    return render(req,'index.html', {'u_name':u_name})

def my_logout(req):
    response = HttpResponseRedirect('/myapp/login')
    response.delete_cookie('u_name')
    return response

def myregister(req):
    if req.method == 'GET':
        return render(req, 'register.html')
    else:
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')
        # 判断用户的输入是否满足基本要求
        if u_name and len(u_name)>3 and pwd and confirm_pwd and pwd==confirm_pwd:
            # 判断是否被注册
            exists_flag = MyUser.objects.filter(username=u_name).exists()
            if exists_flag:
                return HttpResponse('该用户不可用')
            else:
                user = User.objects.create_user(username=u_name, password=pwd)
                return HttpResponse(  '创建成功'+ user.username)