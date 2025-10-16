#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :__init__.py.py
# @Time :2025/10/10 16:51
# @Author :jzk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from common.config import Config

app = FastAPI()

# 跨域问题
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许跨域的域名
    allow_credentials=True,  # 是否允许携带cookie
    allow_methods=["*"],  # 允许请求的方法，比如get、post
    allow_headers=["*"],  # 允许携带的头，比如authorization，content-type
)

from api import adminApi, exceptionHandler,courseApi,studentApi
