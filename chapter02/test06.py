from fastapi import (FastAPI,
                     Cookie)
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title='cookie API',
    description='获取cookie的值'
)


@app.post('/get_cookie',
          tags=['获取cookie'],
          summary='获取cookie',
          response_description='获取了cookie',
          )
def get_cookie(userid: str = Cookie(None)):
    return '获取cookie的值' + userid


class User(BaseModel):
    id: int = None
    name: str


@app.post('/login',
          tags=['设置cookie'],
          summary='设置cookie',
          response_description='设置了cookie',
          )
def login(user: User):
    if user.name == 'Gino':
        content = {'code': 200, 'msg': '登录成功'}
        rsp = JSONResponse(content=content)
        rsp.set_cookie(key='username', value='Gino')
        return rsp
    else:
        return JSONResponse(content={'code': 302, 'msg': '登录失败'})


@app.get('/login2',
         tags=['设置cookie'],
         summary='演示设置cookie',
         response_description='演示设置了cookie',
         )
def login2(name: str):
    if name == 'Gino':
        content = {'code': 200, 'msg': '登录成功'}
        rsp = JSONResponse(content=content)
        rsp.set_cookie(key='username', value='Gino')
        return rsp
    else:
        return JSONResponse(content={'code': 302, 'msg': '登录失败'})
