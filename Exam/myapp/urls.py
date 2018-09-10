from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register$', register, name='register'),
    url(r'^login$', my_login, name='login'),
    url(r"^active/(.+)", active, name="active"),
    url(r"^index/", index, name="index"),
    url(r"^inf/", inf, name="inf"),
    url(r"^person/<(\d+)>/", inf, name="inf"),

]
