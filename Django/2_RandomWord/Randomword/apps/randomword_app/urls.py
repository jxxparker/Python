from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word/$', views.word),
    url(r'^random_word/reset$', views.reset)
]