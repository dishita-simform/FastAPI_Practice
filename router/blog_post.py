from fastapi import APIRouter

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.post('/create')
def create_blog():
    return {'message' : 'Blog Created!'}