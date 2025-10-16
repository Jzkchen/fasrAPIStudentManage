#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :course.py
# @Time :2025/10/11 15:57
# @Author :jzk
from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from model import Base


class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    number: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    periods: Mapped[str] = mapped_column(String(255), nullable=False)
    teacher: Mapped[str] = mapped_column(String(255), nullable=False)

class CourseQuery(BaseModel):
    id: int | None = None
    name: str | None = None
    number: str | None = None
    description: str | None = None
    periods: str | None = None
    teacher: str | None = None
