import uvicorn
from fastapi import FastAPI
from enum import Enum

app = FastAPI(
    title='Gino API文档',
    description='内部办公网 API文档',
    openapi_url='/openApi.json'
)


@app.get('/')
def get_user():
    return 'hello fastapi'


# 路径参数
@app.get('/user/{id}')
def get_user(id: int):
    return id


# 路径参数
@app.get('/user/{id: path}')
def get_user(id: str):
    return id


# 路径参数
@app.get('/user2/{info: path}')
def get_user(info: str):
    return info


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    unknow = 'unknow'


@app.get('/user3/{gender}')
def get_user_gender(gender: Gender):
    return gender


if __name__ == '__main__':
    # uvicorn.run(app='test01:app', reload=True, host='0.0.0.0', port=8080, debug=True)
    uvicorn.run(app='test01:app')
