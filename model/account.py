#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :account.py
# @Time :2025/10/13 15:51
# @Author :jzk
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AccountLogin(BaseModel):
    username: str
    password: str
    role: str

class AccountLoginResponseModel:
    id: int
    username: str
    role: str
    name:str
    token: str

class AccountRegister(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    gender: Optional[int] = None
    phone: Optional[int] = None
    birthday: Optional[datetime] = None  # ✅ 改为可选
    role: Optional[str] = None
