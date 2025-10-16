#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :customException.py
# @Time :2025/10/10 19:52
# @Author :jzk

class UserNotFoundException(Exception):
    def __init__(self, message:str):
        self.message = message

class PasswordNotMatchException(Exception):
    def __init__(self, message:str):
        self.message = message

class TokenException(Exception):
    def __init__(self, message:str):
        self.message = message

class ServiceErrorException(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class CourseExistingException(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class CourseNotExistException(Exception):
    def __init__(self, message:str):
        super().__init__(message)