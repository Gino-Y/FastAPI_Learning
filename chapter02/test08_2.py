from fastapi import FastAPI, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from chapter02 import test08_utils

from datetime import timedelta

EXPIRE_MINUTE = 60

app08_2 = APIRouter(prefix='/token',
                     tags=['token认证'])


# 登录：获取用户名密码并校验，校验通过返回token
@app08_2.post("/login",
              summary='登录、校验、回token',
              response_description='登陆（成功或失败）状态')
def login(user: OAuth2PasswordRequestForm = Depends()):
    """
    登录：获取用户名密码并校验，校验通过返回token \n
    """
    username = user.username
    password = user.password
    # 密码加密
    hash_pwd = test08_utils.get_hash_pwd(password)

    # todo 用户名密码校验
    is_ok = True  # 假如用户名密码证通过

    expire_time = timedelta(minutes=EXPIRE_MINUTE)
    if is_ok:
        # 生成token,假如username是唯一的
        token = test08_utils.create_token({"sub": id}, expire_time)

        return {"code": 200, "msg": "登陆成功", "token": token}
    else:
        return {"code": 401, "msg": "登录失败"}


@app08_2.get("/list")
def get_list(user: str = Depends(test08_utils.parse_token)):
    return user
