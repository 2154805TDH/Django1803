from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.views.decorators.cache import cache_page

from .models import *
from django.views.generic import View
# from django.core.cache import cache
from .my_util import send_verify_mail
from django_redis import get_redis_connection
SUCCESS = 1
FAIL = 2

DATA = {
    'code': SUCCESS,
    'msg': 'ok',
    'data': ''
}

class RegisterAPI(View):

    def post(self, req):
        # 解析参数
        param = req.POST
        u_name = param.get("u_name")
        pwd = param.get("pwd")
        confirm_pwd = param.get("pwd_confirm")
        email = param.get("email")
        icon = req.FILES['icon']

        # 对数据做校验
        if len(u_name) <= 4:
            return HttpResponse("账号名过短")
        if pwd and len(pwd) > 0 and pwd == confirm_pwd:
            if MyUser.objects.filter(username=u_name).exists():
                return HttpResponse("用户已存在")
            else:
                # 创建用户
                user = MyUser.objects.create_user(
                    username=u_name,
                    password=pwd,
                    email=email,
                    is_active=False,
                    icon=icon
                )
                #生成验证连接 发送邮件
                token = send_verify_mail(email, req.get_host())
                # 记录邮件和随机字符的验证邮箱
                cache.set(token, user.id, settings.EMAIL_TOKEN_MAX_AGE)
                return redirect(reverse("axf:login_view"))


#登录API
# class LoginAPI(View):
#     def post(self, req):
#         params = req.POST
#         # 'user_name': u_name,
#         # 'pwd': enc_data
#         # 解析参数
#         u_name = params.get("user_name")
#         pwd = params.get("pwd")
# #         校验数据
#         if pwd and u_name and len(u_name) >= 4:
#             # 校验用户
#             user = authenticate(username=u_name, password=pwd)
#             if user:
#                 # 校验通过 就让用户登录
#                 login(req, user)
#                 # 返回跳转的连接
#                 DATA['data'] = "/axf/mine"
#                 return JsonResponse(DATA)
#             else:
#                 # 如果校验失败 给出提示信息
#                 DATA['code'] = FAIL
#                 DATA['msg'] = '账号或密码错误'
#                 return JsonResponse(DATA)
#         else:
#             DATA['code'] = FAIL
#             DATA['msg'] = "账号或密码不能为空"
#             return JsonResponse(DATA)


def active(req, token):
    # 在缓存尝试拿数据
    token1 = token
    print(token1, type(token1))
    user_id = cache.get(token1)
    name = cache.get('name')
    print(name)
    print(user_id)
    if user_id:
        # 如果拿到用户 那就修改用户的激活状态
        MyUser.objects.filter(pk=int(user_id)).update(is_active=True)
        # return redirect(reverse("axf:login_view"))
        return HttpResponse('ok')
    else:
        return HttpResponse("链接不正确或失效")


# class LogoutAPI(View):
#
#     def get(self, req):
#         # 退出
#         logout(req)
#         return redirect(reverse('axf:home'))