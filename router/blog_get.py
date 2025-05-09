from enum import Enum
from typing import Optional
from fastapi import APIRouter, Response, status, Depends

from router.blog_post import required_function

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

#Path Parameters
@router.get('/{id}',status_code=status.HTTP_200_OK)
def blog_id(id:int, response:Response):
       #Will Be Used as Description in Swagger UI
    """
    Get Blogs by ID
    - **id**: ID of the blog
    """
    if id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message' : f'Blog ID {id} Not Found!'}
    else :
        response.status_code = status.HTTP_200_OK
        return {'message' : f'Blog ID {id} Found!'}

#Path Parameters with Options
class BlogType(str, Enum):
    blog = "blog"
    news = "news"
    article = "article"
    short= "short"
    tutorial = "tutorial"

@router.get('/type/{type}')
def get_blog_type(type : BlogType,req_parameter:dict = Depends(required_function)):
    return {'message' : f'Blog Type is {type}, Required Function is {req_parameter}'}

#Normal Query Parameters
@router.get('/all/normal', tags=['Parameters'])
def get_blogs_normal(page,page_size):
    return {'message' : f'Page is {page} and Page Size is {page_size} (Normal)'}

#Default Query Parameters
@router.get('/all/default', tags=['Parameters'])
def get_blogs_default(page=1,page_size=15):
    return {'message' : f'Page is {page} and Page Size is {page_size} (Default)'}

#Optional Query Parameters
@router.get('/all/optional', tags=['Parameters'])
def get_blogs_optional(page=1,page_size:Optional[int]=None):
    return {'message' : f'Page is {page} and Page Size is {page_size} (Optional)'}

#Query & Path Parameters Hybrid
@router.get('/{id}/comments/{comment_id}', tags=['Parameters', 'Comments'])
def get_comment(id:int, comment_id:int, valid:bool = True, username:Optional[str]=None):
    return {'message' : f'Blog ID is {id}, Comment ID is {comment_id}, Valid is {valid} and Username is {username}'}