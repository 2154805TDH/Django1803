from django.contrib.auth.backends import ModelBackend
from .models import MyUser

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 找用户
        # 做认证
        user = None
        try:
            user = MyUser.objects.get(username=username)
        except:
            try:
                user = MyUser.objects.get(phone=username)
            except:
                try:
                    user = MyUser.objects.get(email=username)
                except:
                    return None
        if user.check_password(password):
            return user
        else:
            return None