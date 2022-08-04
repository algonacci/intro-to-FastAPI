from unicodedata import category
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None


class Post(BaseModel):
    title: str
    content: str
    category: str


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}


@app.post('/post/{post_id}')
def post_something(post_id: int, post: Post):
    return {"post_id": post_id, "title": post.title, "content": post.content, "category": post.category}
