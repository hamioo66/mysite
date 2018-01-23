# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/22
describle:
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.get_details, name='detailblog'),
]

