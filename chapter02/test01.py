import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='Gino API文档',
    description='内部办公网 API文档',
    openapi_url='/openApi.json'
)


# @app.get('/')
# def get_user():
#     return 'hello fastapi'


# # 路径参数
# @app.get('/user/{id}')
# def get_user(id: int):
#     return id


# 路径参数
@app.get('/user/{id: path}')
def get_user(id: str):
    return id


if __name__ == '__main__':
    uvicorn.run(app='test01:app', reload=True, host='0.0.0.0', port=8080, debug=True)
