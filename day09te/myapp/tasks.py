from celery import task
from django.conf import settings
import time

from django.core.mail import send_mail


@task
def hello_celery(loopnum):
    for i in range(loopnum):
        print('hello')
        time.sleep(2)


@task
def send_email(email):
    title = '没有标题'
    msg = '恭喜你注册成功'
    from_email = settings.DEFAULT_FROM_EMAIL
    recievers = [email, ]
    send_mail(
        title,
        msg,
        from_email,
        recievers,
        fail_silently=True
    )
