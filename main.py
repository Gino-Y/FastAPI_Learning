import uvicorn
from fastapi import FastAPI, Request
from chapter02 import app01, app03, app04, app05, app06, app08, app08_2, app10

app = FastAPI(
    title='Gino API文档',
    description='This is an interface interaction test document',
    openapi_url='/openApi.json'
)
app.include_router(app01)
app.include_router(app03)
app.include_router(app04)
app.include_router(app05)
app.include_router(app06)
app.include_router(app08)
app.include_router(app08_2)
app.include_router(app10)


# app.include_router(app09)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 路径参数
@app.get('/user/{id}')
def get_user(id: int):
    return id


# # 路径参数
# @app.get('/user/{id: path}')
# def get_user(id: str):
#     return id

# 自定义中间件
@app.middleware("http")
async def set_cookie(request: Request, call_next):
    print(request.client.host)
    print(request.client.port)
    print(request.url)
    print(request.method)
    print(request.headers["Host"])
    print(request.headers["User-Agent"])
    # print(request.query_params["name"])
    # print(request.path_params["id"])
    print(request.cookies.get("username"))
    response = await call_next(request)
    response.headers["name"] = "hallen"
    response.set_cookie(key="username", value="Gino")
#
    print("=============")
    print(response.status_code)
    return response


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, workers=1)
