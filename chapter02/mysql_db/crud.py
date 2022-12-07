from sqlalchemy.orm import Session
from chapter02.mysql_db.user_model import User


# 增
def add_user(db: Session, username: str):
    user = User(username=username)
    db.add(user)  # add([])
    db.commit()
    db.flush()
    db.refresh(user)


# 改：先查再改
def update_user(db: Session, user_id: int, username: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        db.commit()
        db.flush()
        db.refresh(user)


# 删:先查再删
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        db.delete(user)
        db.commit()
        db.flush()


# 查
def get_user_by_id(db: Session, user_id: int) -> User:
    user = db.query(User.id, User.username).filter(User.id == user_id).first()
    return user


def get_users_by_name(db: Session, username: str) -> [User]:
    users = db.query(User.id, User.username).order_by(User.id.desc()).filter_by(username=username).all()
    # count = db.query(User.id, User.username).order_by(User.id.desc()).filter_by(username=username).count()
    return users
