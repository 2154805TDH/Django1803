from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^firsttask$', first_task),
    url(r'^send_email$', send_email),
]