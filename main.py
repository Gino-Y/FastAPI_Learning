import uvicorn
from fastapi import FastAPI
from chapter02 import app01, app03, app04, app05, app06, app08
from chapter02.test08_2 import app08_2

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

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, workers=1)
