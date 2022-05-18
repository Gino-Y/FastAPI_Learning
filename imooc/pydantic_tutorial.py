from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional




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
