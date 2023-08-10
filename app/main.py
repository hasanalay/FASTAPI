from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from httpx import post
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    Title: str
    Content: str
    Published: bool = True
    Rating: Optional[int] = None

my_posts = [{"Title": "Hello", "Content": "This is the content of the post.", "Published": True, "Rating": 5, "Id": 1},
            {"Title": "Book", "Content": "Those are my books", "Published": True, "Rating": 4, "Id": 2},]

def find_post_by_id(id: int):
    for post in my_posts:
        if post["Id"] == id:
            return post
    return None

@app.get("/")
def root():
    return {"message": "Hello World this is initial page for the FastAPI."}

@app.get("/posts")
def get_posts():
    return {"Data": my_posts}


@app.get("/posts/{id}")
def get_post_by_id(id: int, response: Response):
    if not find_post_by_id(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    return {"Data": find_post_by_id(id)}

@app.post("/posts/create", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["Id"] = randrange(1, 1000)
    my_posts.append(post_dict)
    return {"Data": post_dict}

@app.delete("/posts/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = find_post_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    my_posts.remove(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: Post):
    post_id = find_post_by_id(id)
    if not post_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    post_dict = post.model_dump()
    post_dict["Id"] = id
    return {"Data": post_dict}