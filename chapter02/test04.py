from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title='Response Test',
    description='返回数据的集中方式'
)


@app.get('/ret_str', tags=['返回字符串'])
def ret_str():
    return 'hello fastapi'


@app.get('/ret_dict', tags=['返回字典'])
def ret_dict():
    return {'id': 1, 'mane': 'Gino'}


@app.get('/ret_json', tags=['返回Json'])
def ret_json():
    content = {'id': 1, 'mane': 'Gino'}
    return JSONResponse(content=content)


@app.get('/ret_json2', tags=['返回Json'])
def ret_json():
    """
    这种也不行啊
    :return:
    """
    content = "{'id': 1, 'mane': 'Gino'}"
    return JSONResponse(content=content)


@app.get('/ret_header', tags=['返回到header'])
def ret_header(rsp: Response):
    rsp.headers['name'] = 'Gino'
    return 'hello fastapi'


@app.get('/ret_header2', tags=['返回到header'])
def ret_header():
    content = {'age': 18}
    headers = {'name': 'Gino', 'addr': 'HangZhou'}
    return JSONResponse(content=content, headers=headers)


class Article(BaseModel):
    id: int
    title: str


class User(BaseModel):
    id: int
    name: str
    pwd: str


class RetUser(BaseModel):
    id: int
    name: str


@app.get('/ret_model', tags=['返回模型'])
def ret_model_data():
    article = Article(id=2, title='Article Test')
    return article


@app.get('/ret_model2', tags=['返回模型'], response_model=RetUser)
def ret_model_data():
    user = User(id=1, name='Gino', pwd='123456')
    return user


# @app.get('/ret_model3', tags=['返回模型'], response_model=Union[RetUser, Article])
# def ret_model_data():
#     user = User(id=1, name='Gino', pwd='123456')
#     article = Article(id=2, title='Article Test')
#     return user




















