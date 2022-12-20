import uvicorn

from fastapi import FastAPI, Depends, APIRouter

from chapter02.mysql_db.db import Engine, LocSession, Base
from sqlalchemy.orm import Session
from chapter02.mysql_db import crud

# 创建数据库表结构
Base.metadata.create_all(bind=Engine)


# 初始化db的依赖
def init_db():
    try:
        db = LocSession()
        yield db
    finally:
        db.close()


# app = FastAPI(
#     description="数据库api文档"
# )
app11 = APIRouter(prefix='/api',
                  tags=['数据库api文档'],
                  )


@app11.get("/",
           summary='查, 根据ID查用户信息',
           response_description='查到的用户信息')
async def get_index(user_id: int, db: Session = Depends(init_db)):
    user = crud.get_user_by_id(db, user_id)
    print(user.id)
    print(user.username)
    return user


@app11.get("/get_users",
           summary='查，根据名字查用户信息',
           response_description='查到的用户信息')
async def get_users(username: str, db: Session = Depends(init_db)):
    users = crud.get_users_by_name(db, username)
    for user in users:
        print(user.id)
        print(user.username)
    return users


@app11.post("/add")
async def add_user(username: str, db: Session = Depends(init_db)):
    crud.add_user(db, username)

    return "添加成功"


@app11.post("/update")
async def update_user(user_id: int, username: str, db: Session = Depends(init_db)):
    crud.update_user(db, user_id, username)
    return "更新成功"


@app11.get("/delete")
async def delete_user(user_id: int, db: Session = Depends(init_db)):
    crud.delete_user(db, user_id)
    return "删除成功"


if __name__ == '__main__':
    uvicorn.run(app="test11:app", reload=True, host="0.0.0.0", port=8080)
