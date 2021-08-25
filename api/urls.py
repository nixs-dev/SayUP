from django.conf.urls import url
from . import views

urlpatterns = [
    url('musics', views.MusicList.as_view(), name='music-list'),

]