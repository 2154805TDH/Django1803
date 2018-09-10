from django.http import HttpResponse
from django.shortcuts import render
from .tasks import hello_celery, send_email
# Create your views here.

def first_task(req):
    hello_celery.delay(4)
    send_email.delay('1511128449@qq.com')
    return HttpResponse('ok')

