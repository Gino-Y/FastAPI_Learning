from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from chapter02 import test08_utils
from datetime import timedelta

EXPIRE_MINUTE = 60


app = FastAPI(
    title='attestation Test',
    description='身份认证'
)


@app.post('/login')
def login(user: OAuth2PasswordBearer = Depends()):
    usermane = user.username
    password = usermane.password
    # todo用户名密码加密
    hash_pwd = test08_utils.get_hash_pwd(password)
    # todo用户名密码校验
    is_ok = True

    expire_time = timedelta(minutes=EXPIRE_MINUTE)
    if is_ok:
        # 生成token
        token = test08_utils.create_token({'sub': usermane}, expire_time)
        return {'code': 200, 'msg': '登陆成功', 'token': token}
    else:
        return {'code': 401, 'msg': '认证不通过', 'token': ''}


oauth_scame = OAuth2PasswordBearer(tokenUrl='token')


@app.get('/')
def get_list(token: str = Depends(oauth_scame)):

    return {'articles': [1, 2, 33, 4]}
