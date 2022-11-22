from fastapi import (APIRouter,
                     Body,
                     Form)
from pydantic import BaseModel, Field, HttpUrl

app03 = APIRouter(prefix='/post',
                  tags=['post 响应测试'])


@app03.post('/json_test',
            tags=['Post Test'],
            description='输入一个JSON,后台打印出来,并直接返回',)
def json_test(user: dict):
    """
    输入一个JSON
    后台打印出来
    并直接返回
    :param user: JSON
    :return: JSON
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


@app03.post('/test_post2', tags=['Post Test Use Model'])
def get_post_data_model(user: User = Body(..., embed=True)):
    """
    :param user:
    :return:
    """
    return user


@app03.post('/test_post3', tags=['Post Test Use Model'])
def get_post_data_model(user: User,
                        article: Article):
    """
    :param article:
    :param user:
    :return:
    """
    return {'user': user, 'article': article}


@app03.post('/test_post4', tags=['Post Test Use Model'])
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


@app03.post('/test_post5', tags=['Post Test', 'Form Test'])
def get_post_form(id: int = Form(..., gt=5),
                  name: str = Form(...,
                                   min_length=3,
                                   max_length=10,
                                   description='name的长度不能少与3和超过10个字符')):
    """
    表单数据练习
    :param id:
    :param name:
    :return:
    """
    return {'id': id,
            'name': name}
