from pydantic import BaseModel 
# region Model
# This our input tables model and we use inheritence here.

class PostBase(BaseModel):
    Title: str
    Content: str
    Published: bool = True
    
class PostCreate(PostBase):
    pass

# endregion