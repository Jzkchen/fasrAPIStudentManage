#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :profile.py
# @Time :2025/10/28 15:21
# @Author :jzk
from pathlib import Path


class Profile:
    __file_path = None

    @staticmethod
    def get_profile():
        project_path=Path(__file__).parent.parent  # 获取项目根目录
        file_path=project_path.joinpath('files')  # 拼接文件夹路径
        if not file_path.exists():
            file_path.mkdir(parents=True)  # 如果文件夹不存在则创建
        Profile.__file_path=str(file_path)
        return file_path