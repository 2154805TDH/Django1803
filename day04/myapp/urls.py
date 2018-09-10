from django.conf.urls import url
from .views import (get_teachers, get_teachers_v1, get_teacher,
                    index, indexplus, school_index)

urlpatterns = [
    url(r'^get_teachers/', get_teachers),
    url(r'^index/', index, name='index'),
    url(r'^indexplus/', indexplus, name='indexplus'),
    url(r'^school_index/', school_index, name='school_index'),
    url(r'^get_teachers_v1/', get_teachers_v1, name='get_teachers_v1'),
    url(r'^teacher/(?P<i>\d+)', get_teacher, name='get_teacher')
]