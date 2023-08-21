from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr 
# region  Input Models
# This our input tables model and we use inheritence here.
#for posts
class PostBase(BaseModel):
    Title: str
    Content: str
    Published: bool = True
    
class PostCreate(PostBase):
    pass
#For users
class UserBase(BaseModel):
    Email: EmailStr
    Password: str

class UserCreate(UserBase):
    pass
# for login
class UserLogin(BaseModel):
    Email: EmailStr
    Password: str
# endregion

# region Response Models

class Post(PostBase):
    Id: int 
    CreatedDate: datetime
    
    class Config:
        from_attributes = True
        
class UserOutput(BaseModel):
    Id: int 
    Email: EmailStr
    CreatedDate: datetime
    
    class Config:
        from_attributes = True

#endregion

class Token(BaseModel):
    Access_token: str
    Token_type: str
    
class TokenData(BaseModel):
    Id: Optional[str] = None