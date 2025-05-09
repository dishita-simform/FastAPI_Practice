from enum import Enum
from typing import Optional
from fastapi import FastAPI, Response, status

app = FastAPI()

# Hello World
@app.get('/')
def index():
    str = "Hello World from Variable!"
    return {'message' : str}

#Path Parameters
@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def blog_id(id:int, response:Response):
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

@app.get('/blog/type/{type}')
def get_blog_type(type : BlogType):
    return {'message' : f'Blog Type is {type}'}

#Normal Query Parameters
@app.get('/blog/all/normal')
def get_blogs_normal(page,page_size):
    return {'message' : f'Page is {page} and Page Size is {page_size} (Normal)'}

#Default Query Parameters
@app.get('/blog/all/default')
def get_blogs_default(page=1,page_size=15):
    return {'message' : f'Page is {page} and Page Size is {page_size} (Default)'}

#Optional Query Parameters
@app.get('/blog/all/optional')
def get_blogs_optional(page=1,page_size:Optional[int]=None):
    return {'message' : f'Page is {page} and Page Size is {page_size} (Optional)'}

#Query & Path Parameters Hybrid
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id:int, comment_id:int, valid:bool = True, username:Optional[str]=None):
    return {'message' : f'Blog ID is {id}, Comment ID is {comment_id}, Valid is {valid} and Username is {username}'}