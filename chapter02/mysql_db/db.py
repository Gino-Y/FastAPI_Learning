from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# "mysql+pymysql://用户名:密码@host:port/db_name?charset=utf8"
username = "root"
pwd = "Kadfgo53254G"
host = "47.241.35.150"
port = "3306"
db_name = "test_fatapi"

DB_URI = f"mysql+pymysql://{username}:{pwd}@{host}:{port}/{db_name}?charset=utf8"

# 数据库引擎
Engine = create_engine(DB_URI, echo=True)

# 构建session对象
LocSession = sessionmaker(bind=Engine, autoflush=False, autocommit=False)

# SQLORM基类,创建对象的基类
Base = declarative_base()
