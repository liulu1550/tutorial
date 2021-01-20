#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: 多点笔记
@contact: wouldmissyou@163.com
@time: 2021/1/20 上午10:37
@file: permissions.py.py
@desc: 
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """


def has_object_permission(self, request, view, obj):  # 允许任何请求进行读取
    # 所以我们总是允许GET，HEAD或OPTIONS请求。
    if request.method in permissions.SAFE_METHODS:
        return True
    # 只有该snippet的所有者才允许写权限。
    # 别告诉我你读不懂这句代码和这里的if/else逻辑
    return obj.owner == request.user
