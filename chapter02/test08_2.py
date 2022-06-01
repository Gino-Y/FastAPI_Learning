from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from chapter02 import test08_utils
from datetime import timedelta

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
    if is_ok:
        test08_utils.create_token({'useername': user})
        return {'code': 200, 'msg': '登陆成功', 'token': 'xxxxxxx'}
    else:
        return {'code': 401, 'msg': '认证不通过', 'token': ''}


oauth_scame = OAuth2PasswordBearer(tokenUrl='token')


@app.get('/')
def get_list(token: str = Depends(oauth_scame)):

    return {'articles': [1, 2, 33, 4]}
