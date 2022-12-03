from fastapi import (APIRouter,
                     Body,
                     Form)
from pydantic import BaseModel, Field, HttpUrl

app03 = APIRouter(prefix='/post',
                  tags=['post 响应测试'])


@app03.post('/json_test', tags=['Post Test'])
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
    id: int = Field(..., gt=10, description='id必须大于10')
    name: str

    class Config:
        schema_extra = {
            'id': 15,
            'name': 'Gino'
        }


class Image(BaseModel):
    url: HttpUrl
    src: str

    class Config:
        schema_extra = {
            'url': 'http://127.0.0.1:8000/docs',
            'src': 'chapter/test'
        }


class Article(BaseModel):
    id: int
    title: str
    image: Image


@app03.post('/model_test', tags=['Post Test Use Model'])
def model_test(user: User = Body(..., embed=True)):
    """
    练习使用模型 \n
    Body(..., embed=True) 外层插入key \n
    :param user:使用模型类定义的User类 id必须大于10、gt=10\n
    :return:返回user的值
    """
    return user


@app03.post('/multiple_model', tags=['Post Test Use Model'])
def multiple_model(user: User,
                   article: Article):
    """
    多个模型不需要设置embed=True \n
    :param article: 文章模型 注意url格式不能错 \n
    :param user: 用户模型 \n
    :return: 返回文章和用户模型 \n
    """
    return {'user': user, 'article': article}


@app03.post('/mixture', tags=['Post Test Use Model'])
def mixture(user: User,
            article: Article,
            count: int = Body(...)):
    """
    多字段模型参数和单字段参数同时作为参数的方式 \n
    单字段插入必须使用 = Body(...) \n
    :param count: 单字段参数 \n
    :param article: 文章多字段模型参数 \n
    :param user: 用户多字段模型参数 \n
    :return: 文章多字段模型、用户多字段模型、计数单字段
    """
    return {'user': user,
            'article': article,
            'count': count}


@app03.post('/form_test', tags=['Post Test', 'Form Test'])
def get_post_form(id: int = Form(..., gt=5),
                  name: str = Form(...,
                                   min_length=3,
                                   max_length=10,
                                   description='name的字符长度不能少与3和超过10个字符')):
    """
    表单数据练习 \n
    :param id: ID值 需要大于 5 \n
    :param name: name的长度不能少与3和超过10个字符 \n
    :return: id和name
    """
    return {'id': id,
            'name': name}
