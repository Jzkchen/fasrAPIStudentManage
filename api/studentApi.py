#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :studentApi.py
# @Time :2025/10/16 15:13
# @Author :jzk
from typing import Optional

from fastapi import Depends, APIRouter
from fastapi.params import Query

from api import app
from common.auth import auth_handler
from common.pageHelper import PageHelper
from common.result import ResultModel, Result
from model import get_db_session, Session
from model.account import AccountRegister
from model.student import StudentQuery, StudentCreate, StudentUpdate
from service.studentService import StudentService


@app.post("/register",response_model=ResultModel)
async def register(account: AccountRegister, db_session: Session = Depends(get_db_session)):
    """
    学生注册
    """
    StudentService.register(account, db_session)
    return Result.success()

# student_router = APIRouter(prefix='/student', tags=['student'],dependencies=[Depends(auth_handler.auth_required)])
student_router = APIRouter(prefix='/student', tags=['student'])



@student_router.get("/selectPage", response_model=ResultModel)
async def get_student_list(page: int = Query(1, ge=1, alias='pageNo', description="Page number"),
                          size: int = Query(5, gt=0, le=100, alias='pageSize', description="Page size"),
                          name: Optional[str] = Query(None, description="Student name"),
                          username: Optional[str] = Query(None, description="Student name"),
                          db_session: Session = Depends(get_db_session)
                          ):
    pageInfo = PageHelper.startPage(page, size)
    student_query=StudentQuery(name=name,username=username)
    student_list = StudentService.select_page(student_query,db_session)
    result = Result.success(pageInfo.of(student_list))
    return result

@student_router.post("/add",response_model=ResultModel)
async def add_student(student:StudentCreate,db_session: Session = Depends(get_db_session)):
    StudentService.add_student(student,db_session)
    return Result.success()

@student_router.put("/update",response_model=ResultModel)
async def update_student(student:StudentUpdate,db_session: Session = Depends(get_db_session)):
    StudentService.update_student(student,db_session)
    return Result.success()

@student_router.delete("/delete/{id}",response_model=ResultModel)
async def delete_student(student_id:int,db_session: Session = Depends(get_db_session)):
    StudentService.delete_student(student_id,db_session)
    return Result.success()

app.include_router(student_router)