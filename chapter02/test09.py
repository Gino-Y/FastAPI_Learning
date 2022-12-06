import uvicorn
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import Response

# app09 = APIRouter(prefix='/middleware',
#                   tags=['中间件api文档'])
app09 = FastAPI(
    description="中间件api文档"
)


@app09.get("/")
def index():
    return "hello fastapi"


# 自定义中间件
@app09.middleware("http")
async def set_cookie(request: Request, call_next):
    """
    自定义中间件
    :param request:
    :param call_next:
    :return:
    """
    print(request.client.host)
    print(request.client.port)
    print(request.url)
    print(request.method)
    print(request.headers["Host"])
    print(request.headers["User-Agent"])
    print(request.query_params["name"])
    # print(request.path_params["id"])
    print(request.cookies.get("username"))
    response = await call_next(request)
    response.headers["name"] = "hallen"
    response.set_cookie(key="username", value="zhiliao")

    print("=============")
    print(response.status_code)
    return response
