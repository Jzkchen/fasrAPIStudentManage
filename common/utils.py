#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :utils.py 工具类
# @Time :2025/10/11 23:49
# @Author :jzk

# 批量设置对象属性值
# 该方法的作用是将传入字典 data 中的键值对，批量设置到目标对象 obj 的属性上。
# 它会遍历 data 的每一项，以 key 作为属性名、value 作为属性值，动态地为 obj 对象赋值。
# 如果 data 为空，会抛出 ValueError 异常。

def set_attrs(obj, data: dict):
    """设置对象属性值"""
    if not data:
        raise ValueError("data不能为空")
    for key, value in data.items():
        setattr(obj, key, value)
# setattr(obj, key, value) 是一个 Python 内置函数，用于设置对象的属性值。它接受三个参数：
# obj：要设置属性的对象
# key：要设置的属性名
# value：要设置的属性值
# 它会将 obj 对象中名为 key 的属性值设置为 value。
# 如果 obj 对象中没有名为 key 的属性，则会创建一个新的属性，并将其值设置为 value。
# 如果 obj 对象中已经有名为 key 的属性，则会覆盖原有的属性值。
# 如果 value 为 None，则会删除 obj 对象中名为 key 的属性。
# 如果 value 为 None，则会删除 obj 对象中名为 key 的属性。