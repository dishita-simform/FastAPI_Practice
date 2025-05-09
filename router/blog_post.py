from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.post('/create')
def create_blog():
    return {'message' : 'Blog Created!'}

class ImageModel(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
    title:str
    content:str
    published:Optional[bool] = True
    tags:List[str] = []
    metadata:Dict[str,str]={'key1':'value1'}
    image:Optional[ImageModel] = None

@router.post('/new/{id}')
def create_blog (blog:BlogModel, id:int, version: int=1):
    return {
        'message' : 'Blog Created!',
        'id' : id,
        'version' : version,
        'data' : blog
    }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog:BlogModel, id:int, 
                   comment_title:int=Query(None, 
                                        title='Comment Title',
                                        description='Some Random Description for Comment Title',
                                        alias='commentTitle',
                                        deprecated=True),
                                        content: str=Body(...,
                                                          min_length=10, 
                                                          max_length=50,
                                                          regex=r'^[a-z\s]*$'
                                                          ), #Body(Ellipsis) for non-optional parameters
                                                          v:Optional[List[str]] = Query(None), #Query(['1.1', '2.1', '3.1'])
                                                          comment_id: int = Path(..., gt=5, le=15)
                                        ):                                   
    return{
        'blog':blog,
        'id':id,
        'comment_title':comment_title,
        'content':content,
        'version': v,
        'comment_id':comment_id
    }
