from passlib.context import CryptContext

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# 明文密码加密
def get_hash_pwd(pwd: str):
    return crypt_context.hash(pwd)

# 生成token: 用户数据，token过期时间
def create_token(data: dict, expire_time):



# 解析token
