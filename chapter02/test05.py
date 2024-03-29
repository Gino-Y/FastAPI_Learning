from fastapi import (FastAPI,
                     UploadFile,
                     File,
                     Form, APIRouter)
from typing import List

# app = FastAPI(
#     title='upload API',
#     description='单文件、多文件上传的接口'
# )
app05 = APIRouter(prefix='/upload',
                  tags=['单文件、多文件上传的接口'])


@app05.post('/upload',
            # tags=['文件上传'],
            summary='上传一个文件',
            response_description='上传了一个文件',
            )
async def upload(file: UploadFile = File(..., description='选择一个文件，然后可以上传')):
    print(file.file)
    rep = await file.read()
    with open("./upload/chapter02/" + file.filename, 'wb') as f:
        f.write(rep)
    return '上传成功'


@app05.post('/uploads',
            # tags=['文件上传'],
            summary='上传多个文件',
            response_description='上传了多个文件',
            )
async def uploads(files: List[UploadFile] = File(...),
                  username: str = Form(...)):
    print(username)
    for file in files:
        rep = await file.read()
        with open("./upload/chapter02/" + file.filename, "wb") as f:
            f.write(rep)
    return '上传成功'

# def test_a():
#     print('654654654654654654654')
