#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :adminApi.py
# @Time :2025/10/10 16:52
# @Author :jzk
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends

from common.Enum import RoleEnum
from common.result import Result, ResultModel
from api import app
from model import Session, get_db_session
from model.account import AccountLogin
from model.admin import AdminModel
from service.adminService import AdminService
from service.studentService import StudentService


@app.post("/login",response_model=ResultModel)
async def login(account: AccountLogin,db_session:Session=Depends(get_db_session)):
    if RoleEnum.ADMIN.__eq__(account.role):
        db_account = AdminService.login(account,db_session)
    elif RoleEnum.STUDENT.__eq__(account.role):
        db_account = StudentService.login(account,db_session)
    else:
        return Result.error("角色错误")
    return Result.success(jsonable_encoder(db_account))
