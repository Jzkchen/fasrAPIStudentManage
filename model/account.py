#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :account.py
# @Time :2025/10/13 15:51
# @Author :jzk
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
