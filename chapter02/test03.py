from fastapi import (FastAPI,
                     Body,
                     Form)
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(
    title='Gino API文档',
    description='内部办公网 API文档',
    openapi_url='/openApi.json',
)


@app.post('/test_post', tags=['Post Test'])
def get_post_data(user: dict):
    """
    :param user:
    :return:
    """
    print(user)
    return user


# 使用模型
class User(BaseModel):
    id: int = Field(..., gt=10)
    name: str


class Image(BaseModel):
    url: HttpUrl
    src: str


class Article(BaseModel):
    id: int
    title: str
    image: Image


@app.post('/test_post2', tags=['Post Test Use Model'])
def get_post_data_model(user: User = Body(..., embed=True)):
    """
    :param user:
    :return:
    """
    return user


@app.post('/test_post3', tags=['Post Test Use Model'])
def get_post_data_model(user: User,
                        article: Article):
    """
    :param article:
    :param user:
    :return:
    """
    return {'user': user, 'article': article}


@app.post('/test_post4', tags=['Post Test Use Model'])
def get_post_mix(user: User,
                 article: Article,
                 count: int = Body(...)):
    """
    :param count:
    :param article:
    :param user:
    :return:
    """
    return {'user': user,
            'article': article,
            'count': count}


@app.post('/test_post5', tags=['Post Test Use Model'])
def get_post_form(id: int = Form(...),
                  name: str = Form(...)):
    """
    表单数据练习
    :param id:
    :param name:
    :return:
    """
    return {'id': id,
            'name': name}
