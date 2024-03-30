from typing import Union

from fastapi import FastAPI

viplav = FastAPI()


@viplav.get("/")
def read_root():
    return {"Hello": "World"}


@viplav.get("/items/{item_id}")
def read_item(item_id: float, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}