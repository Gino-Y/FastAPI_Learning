from fastapi import FastAPI

app = FastAPI()


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