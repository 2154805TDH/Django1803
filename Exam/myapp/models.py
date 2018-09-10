from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# 自定义用户模型
class MyUser(AbstractUser):
    icon = models.ImageField(
        upload_to='icons',
        verbose_name='图标',
        null=True
    )

class Person(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='名字'
    )
    infor = models.CharField(
        max_length=256,
        verbose_name='信息'
    )