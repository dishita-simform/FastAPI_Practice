from sqlalchemy.orm import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase

def create_user(db:Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db:Session, id:int):
    return db.query(DbUser).filter(DbUser.id == id).first()

def update_user(db:Session, id:int, request:UserBase):
    user=db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)    
    })
    db.commit()
    return 'User Updated'

def delete_user(db:Session, id:int):
    user=db.query(DbUser).filter(DbUser.id == id).first() 
    user.delete(user)
    db.commit()
    return 'User Deleted'