from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title='Response API',
    description='返回数据的几种方式'
)


@app.get('/ret_str',
         tags=['返回字符串'],
         summary='将得到一个字符串',
         response_description='应答一行字符串',
         status_code=status.HTTP_200_OK)  # 状态码设置
def ret_str():
    return 'hello fastapi'


@app.get('/ret_dict',
         tags=['返回字典'],
         summary='将得到一个字典')
def ret_dict():
    return {'id': 1, 'mane': 'Gino'}


@app.get('/ret_json',
         tags=['返回Json'],
         summary='用JSONResponse, 字典转为json')
def ret_json():
    content = {'id': 1, 'mane': 'Gino'}
    return JSONResponse(content=content)


@app.get('/ret_json2',
         tags=['返回Json'],
         summary='字符串转为json(并不成功)',
         deprecated=True)  # 弃用
def ret_json():
    """
    这种也不行啊
    :return:
    """
    content = "{'id': 1, 'mane': 'Gino'}"
    return JSONResponse(content=content)


@app.get('/ret_header',
         tags=['返回到header'],
         summary='将得到一条headers记录')
def ret_header(rsp: Response):
    rsp.headers['name'] = 'Gino'
    return 'hello fastapi'


@app.get('/ret_header2',
         tags=['返回到header', '返回Json'],
         summary='将得到一条JSON数据,和两条headers记录')
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


# @app.get('/ret_model3', tags=['返回模型'], response_model=RetUser)
# def ret_model_data():
#     user = User(id=1, name='Gino', pwd='123456')
#     article = Article(id=2, title='Article Test')
#     return jsonable_encoder('user', article)


@app.get('/ret_jsonable',
         tags=['返回Json'],
         summary='用jsonable_encoder, 字典转为json')
def ret_jsonable():
    content = {'id': 2}
    json_content = jsonable_encoder(content)
    return json_content

















