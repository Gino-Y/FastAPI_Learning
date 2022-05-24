from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='Gino API文档',
    description='内部办公网 API文档',
    openapi_url='/openApi.json'
)


@app.post('/test_post')
def Get_Post_Data(user: dict):
    """
    test: {"id": 1,"name": "Gino"}
    :param user:
    :return:
    """
    print(user)
    return user


# 使用模型
class User(BaseModel):
    id: int
    name: str


@app.post('/test_post2')
def Get_Post_Data_model(user: User):
    """
    :param user:
    :return:
    """
    return user
