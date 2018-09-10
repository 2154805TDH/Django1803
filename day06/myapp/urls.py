from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^login$',my_login),
    url(r'^index$',index, name='index'),
    url(r'^register$',register, name='register'),
    url(r'^get_user_by_num/(\d+)',get_user_by_num, name='get_user_by_num'),
    url(r'^upload$',update_msg, name='update_msg'),
    url(r'^test$',test)
]