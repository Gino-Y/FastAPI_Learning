from fastapi import (FastAPI,
                     UploadFile,
                     File)

app = FastAPI(
    title='upload API',
    description='单文件、多文件上传的接口'
)


@app.post('/upload',
          tags=['单文件上传'],
          summary='上传一个文件',
          response_description='上传了一个文件',
          )
async def upload(file: UploadFile = File(...)):
    print(file.file)
    rep = await file.read()
    # with open("D:/Works/WebProject/FastAPI_Learning01/upload/chapter02/" + file.filename, 'wb') as f:
    with open("../upload/chapter02/" + file.filename, 'wb') as f:
        f.write(rep)
    return '上传成功'












