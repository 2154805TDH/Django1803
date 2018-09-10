from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^get_image', get_verify_img, name='get_image')
]