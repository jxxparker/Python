from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.reroute),
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<number>\d+)$', views.display_edit),
    url(r'^users/(?P<number>\d+)/edit$', views.edit),
    url(r'^users/(?P<number>\d+)/destroy$', views.destroy),
]