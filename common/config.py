
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :config.py
# @Time :2025/10/10 16:33
# @Author :jzk
import os
from pathlib import Path
from dotenv import load_dotenv

class Config:
    _instance = None  # 用于保存单例实例

    def __new__(cls):
        if cls._instance is None:
            # 还没有实例化过，就创建一个
            cls._instance = super().__new__(cls)
        return cls._instance  # 返回同一个实例

    def __init__(self):
        # 为了避免重复加载 .env，可以用一个标志位判断是否初始化过
        if not hasattr(self, "_initialized"):
            dotenv_path = Path(__file__).parent.parent / ".env"
            load_dotenv(dotenv_path=dotenv_path)
            self._env = dict(os.environ)
            self._initialized = True  # 避免重复初始化

    @property
    def env(self):
        return self._env


# 创建单例实例
config = Config()
