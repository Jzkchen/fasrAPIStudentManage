#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :utils.py 工具类
# @Time :2025/10/11 23:49
# @Author :jzk

def set_attrs(obj, data: dict):
    """设置对象属性值"""
    if not data:
        raise ValueError("data不能为空")
    for key, value in data.items():
        setattr(obj, key, value)
