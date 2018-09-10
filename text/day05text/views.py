from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
# 首页
def user_index(req):
    logout(req)
    # user = req.user
    username = req.session.get('username')
    return render(req, 'index.html', {'userName':username})

# 登录
def userLogin(req):
    if req.method == 'GET':
        return render(req, 'userLogin.html')
    else:
        # params参数
        params = req.POST
        u_name = params.get('userName')
        u_password = params.get('userPassword')
        # 校验
        if u_name and len(u_name)>2 and u_password:
            user = authenticate(username=u_name, password=u_password)
            if user:
                login(req, user)
                # 设置session
                req.session['is_login'] = True
                return render(req, 'index.html', context={'userName':u_name})
            else:
                return HttpResponse('账号或密码输入错误')
        else:
            return HttpResponse('账号或密码输入错误')
        # return render(req, 'userLogin.html')

# 注册
def userRegister(req):
    if req.method == 'GET':
        return render(req, 'userRegister.html')
    else:
        params = req.POST
        u_name = params.get('userName')
        u_password = params.get('userPassword')
        confirm_pwd = params.get('confirm_pwd')
        # 校验
        if u_name and len(u_name)>2 and u_password and confirm_pwd and u_password==confirm_pwd:
            # 判断是否被注册
            exists_flag = User.objects.filter(username=u_name).exists()
            # 设置session
            req.session['is_login'] = True
            if exists_flag:
                return HttpResponse('用户名已被使用!')
            else:
                newUser = User.objects.create_user(username=u_name,password=u_password)
                return render(req, 'index.html', context={'userName':u_name})
        else:
            return HttpResponse('输入有误!')

# 退出登录
def userLogout(req):
    logout(req)
    return redirect('/text/user_index')