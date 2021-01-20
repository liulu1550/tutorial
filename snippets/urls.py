#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: 多点笔记
@contact: wouldmissyou@163.com
@time: 2021/1/19 下午3:57
@file: urls.py
@desc: 
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
