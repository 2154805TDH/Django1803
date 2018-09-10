from django.conf.urls import url
from .views import (index, response_index, get_josn, get_2048,
                    my_login, my_index, my_logout, myregister)

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^response_index/', response_index, name='response_index'),
    url(r'^get_josn/', get_josn, name='get_josn'),
    url(r'^get_2048/', get_2048, name='get_2048'),
    url(r'^login/', my_login, name='login'),
    url(r'^my_index/', my_index, name='my_index'),
    url(r'^my_logout/', my_logout, name='logout'),
    url(r'^myregister$', myregister, name='myregister'),
]