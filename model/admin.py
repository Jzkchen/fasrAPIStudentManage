#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :admin.py
# @Time :2025/10/10 19:30
# @Author :jzk
import bcrypt
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from model import Base
from pydantic import BaseModel


class Admin(Base):
    __tablename__ = "admin"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    nmae: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(255), nullable=False)

    def password_check(self, password: str) :
        return bcrypt.checkpw(password.encode(), self.password.encode())
class AdminModel(BaseModel):
    username: str
    password: str

class AdminLoginResponseModel(BaseModel):
    id: int
    username: str
    token: str