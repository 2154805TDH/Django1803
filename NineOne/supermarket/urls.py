from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^mylogin/', mylogin, name='mylogin'),
    url(r'^register/', register, name='register'),
    url(r'^verify_img/', verify_img, name='verify_img'),
]