from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='hello world',
    description='基础练习'
)


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None


@app.get('/',
         tags=['hello world'],
         summary='hello',
         response_description='world',
         )
def hello_world():
    return {'hello': 'world'}


@app.get('/city/{city}')
def result(city: str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}

