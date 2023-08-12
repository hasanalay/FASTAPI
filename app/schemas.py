from datetime import datetime
from pydantic import BaseModel 
# region  Input Models
# This our input tables model and we use inheritence here.
class PostBase(BaseModel):
    Title: str
    Content: str
    Published: bool = True
    
class PostCreate(PostBase):
    pass

# endregion

# region Response Models

class Post(PostBase):
    Id: int 
    CreatedDate: datetime
    
    class Config:
        from_attributes = True

#endregion