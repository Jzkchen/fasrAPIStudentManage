#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :fileApi.py
# @Time :2025/10/28 15:12
# @Author :jzk
import mimetypes
from datetime import datetime
from http.client import responses

from fastapi import APIRouter, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
from werkzeug.utils import secure_filename

from api import app
from common.constant import HOST, PORT
from common.profile import Profile
from common.result import ResultModel, Result
from exception.customException import FileNotFoundException

file_router = APIRouter(prefix='/files', tags=['file'])


@file_router.post("/upload", response_model=ResultModel)
async def upload_file(file: UploadFile):
    """
    文件上传接口
    """
    original_filename = secure_filename(file.filename)
    # 时间戳
    timestamp = int(datetime.now().timestamp())
    unique_filename = f"{timestamp}_{original_filename}"
    file_save_path = Profile.get_profile()

    # 完整的文件保存路径
    file_final_path = file_save_path.joinpath(unique_filename)

    # 将上传的文件保存到指定路径
    with open(file_final_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # 构建文件访问URL
    url = f"http://{HOST}:{PORT}/files/download/{unique_filename}"

    return Result.success(jsonable_encoder({"url": url}))

@file_router.get("/download/{filename}", )
async def download(filename: str):
    """
    文件下载接口
    """
    file_save_path = Profile.get_profile()
    file_path=file_save_path.joinpath(filename)

    if not file_path.exists():
        raise FileNotFoundException(f"File {filename} not found.")
    # 触发文件下载
    # return FileResponse(file_path,media_type='image/png',filename=filename)
    mime_type,_=mimetypes.guess_type(file_path)

    # 创建StreamingResponse以流式传输文件内容
    response=StreamingResponse(
        open(file_path,'rb'),
        media_type=mime_type,
    )
    # 不设置Content-Disposition，避免浏览器触发下载，只显示文件
    return response

app.include_router(file_router)
