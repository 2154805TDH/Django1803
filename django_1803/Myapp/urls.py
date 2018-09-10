from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login$', my_login, name='login'),
    url(r'^logout$', my_logout, name='logout'),
    url(r'^index$', index, name='index'),
    url(r'^register$', register, name='register'),
    url(r'^upload$', upload, name='upload'),
    url(r'^verify_img$', verify_img, name='verify_img'),

]