from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^get_image', get_verify_img , name='get_verify_img'),
    url(r'^mylogin$', mylogin , name='mylogin'),
    url(r'^get_data$', get_data , name='get_data'),
    url(r'^get_players$', get_players , name='get_players'),
]