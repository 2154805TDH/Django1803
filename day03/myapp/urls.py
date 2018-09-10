from django.conf.urls import url
from .views import get_count, get_player,get_player_by_Q

urlpatterns = [
    url(r'^get_count$',get_count),
    url(r'^get_player$',get_player),
    url(r'^get_player_by_Q$',get_player_by_Q),
]
