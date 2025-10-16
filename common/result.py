#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :result.py
# 标准化API接口返回格式
# @Time :2025/10/10 16:42
# @Author :jzk
from pydantic import BaseModel


class ResultBase:
    code: str
    msg: str
    data: dict


# 是一个 Pydantic 模型 继承自 BaseModel 和 ResultBase
class ResultModel(BaseModel, ResultBase):
    ...


class Result:
    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @classmethod
    def success(cls, data: object = None,code: str = "200", msg: str = "success"):
        """
        解释cls 在这里的作用：
        cls 是对 类本身的引用，当你调用 Result.success() 时，Python 实际执行的是Result.success.__func__(Result, data=None, code="200", msg="success")
        为什么要用 cls 而不是直接写 Result()？
        如果以后有人继承 Result 类（比如CustomResult）并重写 success 方法，使用 cls 可以确保调用的是子类的构造函数，而不是父类 Result 的构造函数
        :param data:
        :param code:
        :param msg:
        :return:
        """
        if not data:
            data = {}
        return cls(code, msg, data)

    @classmethod
    def error(cls, code: str = "500", msg: str = "error", data: object = None):
        if not data:
            data = {}
        return cls(code, msg, data)
