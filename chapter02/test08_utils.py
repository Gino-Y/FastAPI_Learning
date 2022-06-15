from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = 'lasdfjlsdfjlasdkjflsadkjflasdjflasdkjkflasdfjlsakdfjalsdjflsdfjlsdkfjlskdjflskdfj'

ALGORITHM = 'HS256'


# 明文密码加密
def get_hash_pwd(pwd: str):
    return crypt_context.hash(pwd)


# 生成token: 用户数据，token过期时间
def create_token(data: dict, expire_time):

    if expire_time:
        expire = datetime.utcnow() + expire_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    data.update({'exp': expire_time})
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return token


# 解析token
def pase_token(data: dict, expire_time):
    jwt.decode()
