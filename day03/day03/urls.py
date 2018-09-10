"""day03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_stu/', views.get_stu),
    url(r'^get_cla/', views.get_cla),
    url(r'^get_tea_by_cla/', views.get_tea_by_cla),
    url(r'^get_cla_by_tea/', views.get_cla_by_tea),
    url(r'^soccer/', include('myapp.urls')),
    url(r'^bank/', include('myappplus.urls')),
]
