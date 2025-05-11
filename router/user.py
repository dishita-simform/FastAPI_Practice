from fastapi import APIRouter, Depends
from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["User"],
)

# Create User
@router.post('/',response_model=UserDisplay)
def create_user(request:UserBase, db: Session=Depends(get_db)):
    return db_user.create_user(db, request)

# Read User

# Update User

# Delete User