from fastapi import FastAPI, Query, Path, APIRouter
from enum import Enum

# app01 = APIRouter()
app01 = APIRouter(prefix='/get',
                  tags=['get 响应测试']
                  )


@app01.get('/')
def get_user():
    return 'hello fastapi'


# 路径参数
@app01.get('/user/{id}')
def get_user(id: int):
    return id


# 路径参数: 3路径转换器
@app01.get('/user/{id: path}')
def get_user(id: str):
    return id


# 路径参数: 3路径转换器
@app01.get('/user2/{info: path}')
def get_user(info: str):
    return info


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    unknow = 'unknow'


@app01.get('/user3/{gender}')
def get_user_gender(gender: Gender):
    return gender


@app01.get('/user4/{gender}')
def get_user_gender(gender: Gender):
    """
    这是一个测试描述
    :param gender:性别
    :return:性别
    """
    return gender


# 查询参数
@app01.get('/user5/')
def Querying_Parameters(username: str,
                        age: int):
    """
    The exercise of querying parameters
    :param age:
    :param username:
    :return:
    """
    return {'username': username,
            'age': age}


# 可选参数
@app01.get('/user6/')
def Default_Parameters(username: str = None,
                       age: int = 0):
    """
    An exercise in default parameters
    :param age:
    :param username:
    :return:
    """
    return {'username': username,
            'age': age}


# 路径参数和查询参数结合使用
@app01.get('/user6/{id}/{name}')
def Default_Path_Parameters(id: int,
                            name: str,
                            age: int,
                            gender: str):
    """
    路径参数和查询参数结合使用
    :param id:
    :param name:
    :param gender:
    :param age:
    :return:
    """
    return {'id': id,
            'name': name,
            'age': age,
            'gender': gender}


# 查询参数Query校验
@app01.get('/nuser7/')
def Query_Checkout(name: str = Query(None,  # 必传为三个点...
                                     max_length=10,
                                     title='我是标题',
                                     description='name的长度不能超过10个字符')):
    return name


# 查询参数Path校验
@app01.get('/nuser8/{id}')
def Path_Checkout(id: int = Path(...,  # 必传为三个点...
                                 gt=5,
                                 title='我是标题',
                                 description='id的值必须大于5')):
    return id
