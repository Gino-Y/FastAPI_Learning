"""
pydantic
"""

from pydantic import BaseModel
from typing import Optional, Union
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class User(BaseModel):
    id: Optional[int]  # 选填
    user_name: str = '佚名'  # 默认值直接加等号赋值
    age: Union[int, float]  # 联合类型
    gender: Gender  # 枚举

    class Config:
        schema_extra = {
            'id': 1, 'user_name': 'Gino', 'age': 19, 'gender': Gender.male
        }


user_1 = User(id=1, user_name='Gino', age=18, gender=Gender.male)
print(user_1)
print(user_1.age)

data = {'id': 2, 'user_name': 'Yan', 'age': 19, 'gender': 'man'}
user_2 = User(**data)
print(user_2)
print(user_2.user_name)
print(user_2.id)
print(user_2.gender)

user_3 = User(user_name='Tina', age=18, gender=Gender.female)
print(user_3)


class MyBaseModel(BaseModel):
    Id: int
    CreateTime: str
    Desc: str
    IsDelete: Optional[int]  # bool: 0 or 1
    IsActivate: Optional[int]

    class Config:
        schema_extra = {
            'Id': 1,
            'CreateTime': '2022',
            'Desc': 'str',
            'IsDelete': 1,  # bool: 0 or 1
            'IsActivate': 1,
        }


schema_0 = {
    'Id': 1,
    'CreateTime': '2022',
    'Desc': 'str',
}


class Article(MyBaseModel):
    Title: Optional[str]


article = Article(**schema_0)
print(article)
