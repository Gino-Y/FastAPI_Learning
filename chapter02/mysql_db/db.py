from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

# "mysql+pymysql://用户名:密码@host:port/db_name?charset=utf8"
username = "root"
pwd = "Qazwsx123"
host = "localhost"
port = "3306"
db_name = "test_fatapi"

# url = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8"%(username,pwd,host,port,db_name)
url = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(username, pwd, host, port, db_name)

# 数据库引擎
Engine = create_engine(url)

# 构建session对象
LocSession = sessionmaker(bind=Engine)

# SQLORM基类,创建对象的基类
Base = declarative_base()
