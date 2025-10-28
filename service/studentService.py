#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :studentService.py
# @Time :2025/10/13 15:57
# @Author :jzk
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

from common.Enum import RoleEnum
from common.auth import auth_handler
from common.utils import set_attrs
from exception.customException import UserNotFoundException, PasswordNotMatchException, UserExistException, \
    CourseNotExistException
from model.account import AccountLogin, AccountLoginResponseModel, AccountRegister
from model.student import Student, StudentQuery, StudentCreate, StudentUpdate


class StudentService:
    @staticmethod
    # 学生登录方法，根据用户名查找学生信息并校验密码，校验成功后生成并返回token
    def login(account: AccountLogin, db_session: Session) -> AccountLoginResponseModel:
        query = select(Student).where(Student.username == account.username)
        existing_admin: Student = db_session.execute(query).scalars().first()
        if not existing_admin:
            raise UserNotFoundException("用户不存在")
        if auth_handler.verify_password(account.password, existing_admin.password) is False:
            raise PasswordNotMatchException("密码错误")
        account_login_response = AccountLoginResponseModel()
        set_attrs(account_login_response, jsonable_encoder(existing_admin))
        account_login_response.token = auth_handler.encode_token(existing_admin.username)
        return account_login_response

    @staticmethod
    def register(account: AccountRegister, db_session: Session) -> Student:
        query=select(Student).where(Student.username == account.username)
        existing_student: Student = db_session.execute(query).scalars().first()
        if existing_student:
            raise UserExistException("用户已存在")
        new_student = Student()

        # 对密码进行哈希加密
        account.password = auth_handler.get_password_hash(account.password)
        account_data = (
            account.model_dump() if hasattr(account, "model_dump") else account.dict()
        )
        new_student = Student(**account_data)
        if new_student.name is None:
            new_student.name = new_student.username
        new_student.role=RoleEnum.STUDENT.name
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        return new_student

    @staticmethod
    def select_page(student_query: StudentQuery, db_session: Session):
        query = select(Student).order_by(Student.id)
        # 模糊查询
        if student_query.username:
            query = query.where(Student.username.like(f"%{student_query.name}%"))
        if student_query.name:
            query = query.where(Student.name.like(f"%{student_query.number}%"))
        result = db_session.execute(query).scalars().all()
        return result

    @staticmethod
    def add_student(student: StudentCreate, db_session: Session):
        query = select(Student).where(Student.username == student.username)
        existing_student: Student = db_session.execute(query).scalars().first()
        if existing_student:
            raise UserExistException("用户已存在")
        student.password = auth_handler.get_password_hash(student.password)
        student = Student(**student.dict())
        if student.name is None:
            student.name = student.username
        student.role = RoleEnum.STUDENT.name

        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        return student

    @staticmethod
    def update_student(student: StudentUpdate, db_session: Session):
        existing_student: Student = check_student_exists(student.id, db_session)
        # ✅ 不要用 jsonable_encoder
        student_data = (
            student.model_dump() if hasattr(student, "model_dump") else student.dict()
        )

        # ✅ 打印调试（第一次可以留着看）
        print("birthday 类型:", type(student_data.get("birthday")), student_data.get("birthday"))

        set_attrs(existing_student, student_data)
        db_session.commit()
        return existing_student

    @staticmethod
    def delete_student(student_id: int, db_session: Session):
        existing_student: Student = check_student_exists(student_id, db_session)
        db_session.delete(existing_student)
        db_session.commit()
        return existing_student


def check_student_exists(student_id: int, db_session: Session) -> Student:
    query = select(Student).where(Student.id == student_id)
    student_id: Student = db_session.execute(query).scalars().first()
    if not student_id:
        raise UserNotFoundException("用户不存在")
    return student_id