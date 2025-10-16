#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :constant.py 用来放常量
# @Time :2025/10/10 16:40
# @Author :jzk
from common.config import config

HOST = config.env.get("HOST")
PORT = config.env.get("PORT")

MYSQL_DIALECT = config.env.get("MYSQL_DIALECT")
MYSQL_HOST = config.env.get("MYSQL_HOST")
MYSQL_PORT =  config.env.get("MYSQL_PORT")
MYSQL_USER = config.env.get("MYSQL_USER")
MYSQL_PASSWORD = config.env.get("MYSQL_PASSWORD")
MYSQL_DATABASE = config.env.get("MYSQL_DATABASE")

ZERO=0

TOKEN_EXPIRE_1_DAY=1
TOKEN_EXPIRE_5_MINUTES=5
TOKEN_EXPIRE_30_SECOND=30
