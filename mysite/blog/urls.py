# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/22
describle:
"""
from django.conf.urls import url
from mysite.blog import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^index/(\d+)/$', views.get_details, name='detailblog'),
]

