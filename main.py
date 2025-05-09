from fastapi import FastAPI
from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

# Hello World
@app.get('/', summary="Hello World", description="This is a Hello World API", response_description="Hello World Response", tags=['Hello'])
def index():
    str = "Hello World from Variable!"
    return {'message' : str}
