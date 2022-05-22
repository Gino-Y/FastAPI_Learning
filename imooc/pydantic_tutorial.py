from datetime import datetime, date
from pydantic import BaseModel, ValidationError, constr
from typing import List, Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel):
    id: int
    name: str = 'Gino'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2022-12-22 12:22',
    'friends': [1, 2, '3']
}

user = User(**external_data)
# print(user.id, user.friends)
# print(repr(user.signup_ts))
# print(user.dict())
#
# print('\033[21m --- 校验失败处理 ---\033[0m')
# try:
#     User(id=1,
#          signup_ts=datetime.today(),
#          friends=[1, 2, 'not number'])
# except ValidationError as e:
#     print(e.json())
#
# print('------------------')
# print(user.dict())
# print(user.json())
# print(user.copy())
# print('------------------')
#
# print(User.__fields__.keys())
# print('------------------')

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyMode(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: List[constr(max_lengh=255)]

    class Config:
        orm_mode = True


co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'imooc.com']
)

print(CompanyMode.from_orm(co_orm))