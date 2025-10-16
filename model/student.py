#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :student.py
# @Time :2025/10/13 15:42
# @Author :jzk
from datetime import datetime

from sqlalchemy import Integer, String,DateTime

from sqlalchemy.orm import Mapped, mapped_column

from model import Base


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    gender: Mapped[int] = mapped_column(Integer, nullable=False)
    phone: Mapped[int] = mapped_column(Integer, nullable=True)
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    role: Mapped[str] = mapped_column(String(255), nullable=False)

