#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :courseService.py
# @Time :2025/10/11 16:07
# @Author :jzk
from os.path import exists

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

from common.utils import set_attrs
from exception.customException import CourseExistingException, CourseNotExistException
from model.course import Course, CourseQuery


class CourseService:

    @staticmethod
    def select_page(course_query: CourseQuery, db_session: Session):
        query = select(Course).order_by(Course.id)
        # 模糊查询
        if course_query.name:
            query = query.where(Course.name.like(f"%{course_query.name}%"))
        if course_query.number:
            query = query.where(Course.number.like(f"%{course_query.number}%"))
        if course_query.teacher:
            query = query.where(Course.teacher.like(f"%{course_query.teacher}%"))
        result = db_session.execute(query).scalars().all()
        return result

    @staticmethod
    def add_course(course: CourseQuery, db_session: Session):
        query = select(Course).where(Course.name == course.name)
        existing_course: Course = db_session.execute(query).scalars().first()
        if existing_course:
            raise CourseExistingException("课程已存在")
        new_course = Course(
            name=course.name,
            number=course.number,
            description=course.description,
            periods=course.periods,
            teacher=course.teacher
        )
        db_session.add(new_course)
        db_session.commit()
        db_session.refresh(new_course)
        return new_course

    @staticmethod
    def update_course(course: CourseQuery, db_session: Session):
        existing_course: Course = check_course_exists(course.id, db_session)
        set_attrs(existing_course, jsonable_encoder(course))
        db_session.commit()
        return existing_course

    @staticmethod
    def delete_course(course_id: int, db_session: Session):
        existing_course: Course = check_course_exists(course_id, db_session)
        db_session.delete(existing_course)
        db_session.commit()
        return existing_course


def check_course_exists(course_id: int, db_session: Session) -> Course:
    query = select(Course).where(Course.id == course_id)
    existing_course: Course = db_session.execute(query).scalars().first()
    if not existing_course:
        raise CourseNotExistException("课程不存在")
    return existing_course
