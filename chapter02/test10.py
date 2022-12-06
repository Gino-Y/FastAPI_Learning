import uvicorn

from fastapi import FastAPI, Depends, APIRouter

# app = FastAPI(
#     description="依赖注入api文档",
#     dependencies=[Depends(),Depends()]
# )
app10 = APIRouter(prefix='/dependencies',
                  tags=['依赖注入api文档'],
                  dependencies=[Depends(), Depends()]
                  )

user = {"user_id": 1, "user_name": "Gino"}


def get_user_by_id(user_id, name):
    print(name)

    user_id_k = user.get("user_id")

    if int(user_id) == int(user_id_k):
        return user.get("user_name")
    else:
        return "没有该用户"


class GetUserById:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


@app10.get("/get_user/{user_id}")
def get_user(user_name: str = Depends(get_user_by_id)):
    return user_name


@app10.get("/get_article/{user_id}")
def get_article(user_name: str = Depends(get_user_by_id)):
    return user_name


@app10.get("/{user_id}")
def get_index(name: str, user_name: str = Depends(get_user_by_id)):
    return user_name


@app10.get("/get_user_info/{user_id}")
def get_user_cls(name: str, user: GetUserById = Depends()):
    return {"user:id": user.user_id, "name": user.name}


# 没有实际意义
@app10.get("/get_depends", dependencies=[Depends(), Depends()])
def get_depends():
    return "hello fastapi"


if __name__ == '__main__':
    uvicorn.run(app="test10:app", reload=True, host="0.0.0.0", port=8080)
