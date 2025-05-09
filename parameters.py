from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# Hello World
@app.get('/')
def index():
    str = "Hello World from Variable!"
    return {'message' : str}

#Path Parameters
@app.get('/blog/{id}')
def blog_id(id:int):
    return {'message' : f'Blog ID is {id}'}

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
