from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str
 
class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True  # Allows returning data in a customized format
