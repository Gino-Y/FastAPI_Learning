from fastapi import (FastAPI,
                     UploadFile,
                     File,
                     Form)
from typing import List

app = FastAPI(
    title='upload API',
    description='单文件、多文件上传的接口'
)


@app.post('/upload',
          tags=['文件上传'],
          summary='上传一个文件',
          response_description='上传了一个文件',
          )
async def upload(file: UploadFile = File(...)):
    print(file.file)
    rep = await file.read()
    with open("./upload/chapter02/" + file.filename, 'wb') as f:
        f.write(rep)
    return '上传成功'


@app.post('/uploads',
          tags=['文件上传'],
          summary='上传多个文件',
          response_description='上传了多个文件',
          )
async def uploads(files: List[UploadFile] = File(...),
                  username:str = Form(...)):
    print(username)
    for file in files:
        rep = await file.read()
        with open("./upload/chapter02/" + file.filename, "wb") as f:
            f.write(rep)
    return '上传成功'












