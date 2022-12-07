from .db import Base

from sqlalchemy import Column, Integer, String


class User(Base):
    # 定义表名称
    __tablename__ = "cms_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    pwd = Column(String(255))
