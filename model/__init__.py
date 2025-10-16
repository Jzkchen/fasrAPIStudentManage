#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :__init__.py.py
# @Time :2025/10/10 17:03
# @Author :jzk
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from common.constant import MYSQL_DIALECT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE


class Base(DeclarativeBase):
    pass

## mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
engine= create_engine(
    f"{MYSQL_DIALECT}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4",
    echo=True,
)

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)

def get_db_session():
    session=Session()
    try:
        yield session
    finally:
        session.close()