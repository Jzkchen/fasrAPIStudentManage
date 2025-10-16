#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :exceptionHandler.py
# @Time :2025/10/10 19:53
# @Author :jzk
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from common.result import Result
from exception.customException import (
    UserNotFoundException,
    PasswordNotMatchException,
    TokenException,
    ServiceErrorException, CourseExistingException, CourseNotExistException
)
from api import app

@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request:Request, exc: UserNotFoundException):
    result=Result.error(code='404',msg=exc.message)
    return JSONResponse(status_code=404,content=jsonable_encoder(result))

@app.exception_handler(PasswordNotMatchException)
async def password_not_match_exception_handler(request:Request, exc: PasswordNotMatchException):
    result=Result.error(code='401',msg=exc.message)
    return JSONResponse(status_code=401,content=jsonable_encoder(result))

@app.exception_handler(TokenException)
async def token_exception_handler(request:Request, exc: TokenException):
    result=Result.error(code='401',msg=exc.message)
    return JSONResponse(status_code=401,content=jsonable_encoder(result))

@app.exception_handler(ServiceErrorException)
async def service_error_exception_handler(request:Request, exc: ServiceErrorException):
    result=Result.error(code='500',msg=exc.message)
    return JSONResponse(status_code=500,content=jsonable_encoder(result))

@app.exception_handler(CourseExistingException)
async def course_existing_exception_handler(request:Request, exc: CourseExistingException):
    result=Result.error(code='400',msg=exc.message)
    return JSONResponse(status_code=400,content=jsonable_encoder(result))

@app.exception_handler(CourseNotExistException)
async def course_not_exist_exception_handler(request:Request, exc: CourseNotExistException):
    result=Result.error(code='404',msg=exc.message)
    return JSONResponse(status_code=404,content=jsonable_encoder(result))
