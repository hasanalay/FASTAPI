from datetime import datetime
from typing import Optional, Type
from pydantic import BaseModel, EmailStr, conint 
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
class UserOutput(BaseModel):
    Id: int 
    Email: EmailStr
    CreatedDate: datetime
    
    class Config:
        from_attributes = True

class Post(PostBase):
    Id: int 
    CreatedDate: datetime
    owner_id: int
    owner: UserOutput
    
    class Config:
        from_attributes = True

class PostOutput(BaseModel):
    Post: Post
    Likes: int
    
    class Config:
        from_attributes = True
#endregion

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    Id: Optional[str] = None
    
class Like(BaseModel):
    post_id: int
    dir: conint(le=1)