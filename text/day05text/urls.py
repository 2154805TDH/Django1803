from django.conf.urls import url
from .views import (user_index, userLogin, userRegister, userLogout)

urlpatterns = [
    url(r'^user_index/', user_index, name='user_index'),
    url(r'^userLogin/', userLogin, name='userLogin'),
    url(r'^userRegister/', userRegister, name='userRegister'),
    url(r'^userLogout/', userLogout, name='userLogout'),
]