#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :adminService.py
# @Time :2025/10/10 19:45
# @Author :jzk
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

from common.auth import auth_handler
from common.utils import set_attrs
from exception.customException import UserNotFoundException, PasswordNotMatchException
from model.account import AccountLogin, AccountLoginResponseModel
from model.admin import AdminModel, Admin, AdminLoginResponseModel


class AdminService:
    @staticmethod
    def login(account: AccountLogin, db_session: Session)-> AccountLoginResponseModel:
        query = select(Admin).where(Admin.username == account.username)
        existing_admin: Admin = db_session.execute(query).scalars().first()
        if not existing_admin:
            raise UserNotFoundException("用户不存在")
        if auth_handler.verify_password(account.password, existing_admin.password) is False:
            raise PasswordNotMatchException("密码错误")
        account_login_response = AccountLoginResponseModel()
        set_attrs(account_login_response, jsonable_encoder(existing_admin))
        account_login_response.token = auth_handler.encode_token(existing_admin.username)
        return account_login_response
