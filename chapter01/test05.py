"""
pydantic
"""

from pydantic import BaseModel, ValidationError, validator
from pydantic.errors import PydanticValueError
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

data = {'id': 2, 'user_name': 'Yan', 'age': 19, 'gender': Gender.male}
user_2 = User(**data)
print(user_2)
print(user_2.user_name)
print(user_2.id)
print(user_2.gender)

user_3 = User(user_name='Tina', age=18, gender=Gender.female)
print(user_3)


class Required(PydanticValueError):
    code = 'valid_required'
    msg_template = 'Required Field, Current value: {value}'


class IsNotInteger(PydanticValueError):
    code = 'not integer'
    msg_template = 'Value is not integer, Current value: {value}'


class IsNot3(PydanticValueError):
    code = 'not 3'
    msg_template = 'Value is not 3, Current value: {value}'


class MyBaseModel(BaseModel):
    Id: int
    CreateTime: str
    Desc: str
    IsDelete: Optional[int]  # bool: 0 or 1
    IsActivate: Optional[int]

    @validator('Id')
    def valid_id(cls, v):
        if v != 3:
            raise IsNot3(value=v)
        if type(v) == int:
            raise IsNotInteger(value=v)
        if v is None:
            raise Required(value=v)
        if v != 2:
            raise ValueError('id的值不是2')
        return v

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


try:
    article = Article(**schema_0)
    print(article)
except ValidationError as e:
    print(e.errors())
    print(e.json())

print('-----------------------')
print('article2')
try:
    article2 = Article(CreateTime='2022', Desc='描述', Title='名头')
    print(article2)
except ValidationError as e:
    print(e.errors())
    print(e.json())
    # print(str(e))

print('-----------------------')
print('article3')
try:
    article3 = Article(Id=4, CreateTime='2022', Desc='描述', Title='名头')
    print(article3)
except ValidationError as e:
    print(e.errors())
    print(e.json())
    # print(str(e))
