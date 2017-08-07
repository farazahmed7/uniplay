from django.conf.urls import url, include
from spinder import views

__author__ = 'abc'



urlpatterns = [
    url(r'^create/$', views.create_game, name='join_game'),
        url(r'^login/$', views.mobile_facebook_login, name='join_game'),
        url(r'^create/$', views.create_game, name='join_game'),
        url(r'^token/$', views.get_token, name='get_token'),





    url(r'^accounts/', include('allauth.urls')),



]

