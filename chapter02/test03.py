from fastapi import FastAPI, Body
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
def Get_Post_Data_model(user: User = Body(..., embed=True)):
    """
    {
    "user":{
             "id": 0,
             "name": "string"
           }
    }
    :param user:
    :return:
    """
    return user


class Article(BaseModel):
    id: int
    title: str


@app.post('/test_post3')
def Get_Post_Data_model(user: User,
                        article: Article):
    """
    :param article:
    :param user:
    :return:
    """
    return {'user': user, 'article': article}