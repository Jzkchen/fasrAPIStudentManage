#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :Enum.py
# @Time :2025/10/13 16:08
# @Author :jzk
from enum import Enum


class RoleEnum(str,Enum):
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
