from django.conf.urls import url, include
from spinder import views

__author__ = 'abc'



urlpatterns = [
    url(r'^create/$', views.create_game, name='join_game'),


    url(r'^accounts/', include('allauth.urls')),



]

