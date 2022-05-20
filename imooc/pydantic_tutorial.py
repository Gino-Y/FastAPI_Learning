from datetime import datetime, date
from pydantic import BaseModel, ValidationError
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
print(user.id, user.friends)
print(repr(user.signup_ts))
print(user.dict())

print('\033[21m --- 校验失败处理 ---\033[0m')
try:
    User(id=1,
         signup_ts=datetime.today(),
         friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())

print('------------------')
print(user.dict())
print(user.json())
print(user.copy())
print('------------------')

print(User.__fields__.keys())
print('------------------')

