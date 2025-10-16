#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :responseCodeEnum.py 状态码枚举
# @Time :2025/10/11 13:42
# @Author :jzk
from enum import Enum


class ResponseCodeEnum(Enum):
    CODE_200 = ("200", "请求成功")
    CODE_404 = ("404", "请求地址不存在")
    CODE_600 = ("600", "请求参数错误")
    CODE_601 = ("601", "信息已经存在")
    CODE_500 = ("500", "服务器返回错误，请联系管理员")
    CODE_901 = ("901", "登录超时，请重新登录")


    def __init__(self, code: str, msg: str):
        self._code = code
        self._msg = msg

    @property
    def code(self) -> str:
        """获取响应码"""
        return self._code

    @property
    def msg(self) -> str:
        """获取提示信息"""
        return self._msg

    def to_dict(self) -> dict:
        """将枚举转换为字典，方便 FastAPI JSON 序列化"""
        return {"code": self.code, "msg": self.msg}

    @classmethod
    def get_by_code(cls, code: str):
        """根据 code 获取枚举实例"""
        for item in cls:
            if item.code == code:
                return item
        return None

    def __str__(self):
        """打印更友好的字符串形式"""
        return f"{self.name}({self.code}, '{self.msg}')"