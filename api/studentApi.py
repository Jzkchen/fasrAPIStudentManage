#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :studentApi.py
# @Time :2025/10/16 15:13
# @Author :jzk
from fastapi import Depends

from common.result import ResultModel, Result
from model import get_db_session, Session
from model.account import AccountRegister
from service.studentService import StudentService


@app.post("/register",response_model=ResultModel)
async def register(account: AccountRegister, db_session: Session = Depends(get_db_session)):
    """
    学生注册
    """
    StudentService.register(account, db_session)
    return Result.success()
