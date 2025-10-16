#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :courseApi.py
# @Time :2025/10/11 16:01
# @Author :jzk
from typing import Optional

from fastapi import APIRouter
from fastapi.params import Depends, Query
from sqlalchemy.orm import Session

from api import app
from common.auth import auth_handler
from common.pageHelper import PageHelper
from common.result import ResultModel, Result
from model import get_db_session
from model.course import CourseQuery
from service.courseService import CourseService

course_router = APIRouter(prefix='/course', tags=['course'],dependencies=[Depends(auth_handler.auth_required)])


@course_router.get("/selectPage", response_model=ResultModel)
async def get_course_list(page: int = Query(1, ge=1, alias='pageNo', description="Page number"),
                          size: int = Query(5, gt=0, le=100, alias='pageSize', description="Page size"),
                          name: Optional[str] = Query(None, description="Course name"),
                          number: Optional[str] = Query(None, description="Course number"),
                          teacher: Optional[str] = Query(None, description="Course teacher"),
                          db_session: Session = Depends(get_db_session)
                          ):
    pageInfo = PageHelper.startPage(page, size)
    course_query=CourseQuery(name=name,number=number,teacher=teacher)
    course_list = CourseService.select_page(course_query,db_session)
    result = Result.success(pageInfo.of(course_list))
    return result

@course_router.post("/add",response_model=ResultModel)
async def add_course(course:CourseQuery,db_session: Session = Depends(get_db_session)):
    CourseService.add_course(course,db_session)
    return Result.success()

@course_router.put("/update",response_model=ResultModel)
async def update_course(course:CourseQuery,db_session: Session = Depends(get_db_session)):
    CourseService.update_course(course,db_session)
    return Result.success()

@course_router.delete("/delete/{id}",response_model=ResultModel)
async def delete_course(course_id:int,db_session: Session = Depends(get_db_session)):
    CourseService.delete_course(course_id,db_session)
    return Result.success()

app.include_router(course_router)
