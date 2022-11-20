import uvicorn
from fastapi import FastAPI
from chapter02 import app01, app03

app = FastAPI(
    title='Gino API文档',
    description='This is a interface test document',
    openapi_url='/openApi.json'
)
app.include_router(app01, prefix='/get', tags=['get 响应测试'])
app.include_router(app03, prefix='/post', tags=['Post 响应测试'])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 路径参数
@app.get('/user/{id}')
def get_user(id: int):
    return id


# # 路径参数
# @app.get('/user/{id: path}')
# def get_user(id: str):
#     return id

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, workers=1)
