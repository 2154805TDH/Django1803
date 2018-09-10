from django.conf.urls import url
from .apis_v1 import *

urlpatterns = [
    url(r"^register$", RegisterAPI.as_view(), name='api_register'),
    url(r"^active/(.+)", active, name='active'),
]