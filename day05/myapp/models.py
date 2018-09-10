from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        verbose_name='手机号',
        unique=True
    )
    icon = models.ImageField(
        upload_to='icons',
        null=True
    )