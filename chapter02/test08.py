from fastapi import FastAPI, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

# app = FastAPI(
#     title='attestation Test',
#     description='身份认证'
# )
app08 = APIRouter(prefix='/attestation',
                  tags=['身份认证'])


@app08.post('/token')
def get_token(data: OAuth2PasswordBearer = Depends()):
    usermane = data.username
    password = data.password
    # todo用户名密码校验
    is_ok = True
    if is_ok:
        return {'code': 200, 'token': 'xdaqweq', 'msg': '认证通过'}
    return {'code': 401, 'token': '', 'msg': '认证不通过'}


oauth_scame = OAuth2PasswordBearer(tokenUrl='token')


@app08.get('/')
def get_list(token: str = Depends(oauth_scame)):
    return {'articles': [1, 2, 33, 4]}
