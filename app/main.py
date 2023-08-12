import time
from fastapi import Body, Depends, FastAPI, Response, status, HTTPException
from httpx import post
from pydantic import BaseModel 
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# region Models
class Post(BaseModel):
    Title: str
    Content: str
    Published: bool = True
# endregion
# region Db Connection
# Connection to PostgreSQL DB
while True:
    try:
        connection = psycopg2.connect(host='localhost', database='fastapi', user='hasanalay', password='1973', cursor_factory=RealDictCursor)
        cursor = connection.cursor()
        print("Connection to PostgreSQL DB successful")
        break
    except Exception as e:
        print(f"The error '{e}' occurred")
        time.sleep(2)
# endregion
#region Requests
@app.get("/")
def root():
    return {"message": "Hello World this is initial page for the FastAPI."}

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    return {"Data": posts}

@app.get("/posts/{id}")
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.Id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    return {"Data": post}

@app.post("/posts/create", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"Data": new_post}

@app.delete("/posts/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.Id == id).delete(synchronize_session=False)
    db.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.Id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
        
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return {"Data": post_query.first()}
#endregion