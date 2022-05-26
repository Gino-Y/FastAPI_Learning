from fastapi import (FastAPI,
                     Cookie)

app = FastAPI(
    title='cookie API',
    description='获取cookie的值'
)


@app.post('/get_cookie',
          tags=['获取cookie'],
          summary='获取cookie',
          response_description='获取了cookie',
          )
def get_cookie(userid: str = Cookie(None)):
    return '获取cookie的值' + userid
