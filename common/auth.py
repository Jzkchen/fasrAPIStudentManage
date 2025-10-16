#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :auth.py
# @Time :2025/10/10 22:41
# @Author :jzk
from datetime import datetime, timedelta

import jwt
from fastapi.params import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from sqlalchemy.util import deprecated

from common.constant import TOKEN_EXPIRE_1_DAY,ZERO
from exception.customException import TokenException, ServiceErrorException


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 这里可以添加密码加密的上下文，比如使用passlib
    secret = "SECRET"

    # 生成密码的hash,这里使用bcrypt算法
    def get_password_hash(self, password: str) -> str:
        """
        生成hash密码
        :param password: 明文密码
        :return: hash密码
        """
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        验证密码是否匹配
        :param plain_password: 明文密码
        :param hashed_password: hash密码
        :return: 是否匹配
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_name):
        """
        生成JWT Token
        这里使用HS256算法进行加密
        载荷中包含过期时间、签发时间和主题（用户ID）
        :param user_id:
        :return:
        """
        payload = {
            "exp": datetime.utcnow()+timedelta(days=TOKEN_EXPIRE_1_DAY,minutes=ZERO,seconds=ZERO), # 过期时间
            "iat": datetime.utcnow(),# 签发时间
            "sub": user_name # 主题
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise TokenException("登录状态过期")
        except jwt.InvalidTokenError:
            raise ServiceErrorException("系统错误，请联系管理人员")

    def auth_required(self, auth:HTTPAuthorizationCredentials=Security(security)):
        return self.decode_token(auth.credentials)



auth_handler = AuthHandler()