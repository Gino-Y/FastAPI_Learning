from fastapi import FastAPI

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

