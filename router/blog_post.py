from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.post('/create')
def create_blog():
    return {'message' : 'Blog Created!'}

class BlogModel(BaseModel):
    title:str
    content:str
    published:Optional[bool] = True

@router.post('/new/{id}')
def create_blog (blog:BlogModel, id:int, version: int=1):
    return {
        'message' : 'Blog Created!',
        'id' : id,
        'version' : version,
        'data' : blog
    }
