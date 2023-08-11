import time
from fastapi import Body, FastAPI, Response, status, HTTPException
from httpx import post
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

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
        connection = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1234', cursor_factory=RealDictCursor)
        cursor = connection.cursor()
        print("Connection to PostgreSQL DB successful")
        break
    except Exception as e:
        print(f"The error '{e}' occurred")
        time.sleep(2)
# endregion
# I am Going to delete this part.
my_posts = [{"Title": "Hello", "Content": "This is the content of the post.", "Published": True, "Rating": 5, "Id": 1},
            {"Title": "Book", "Content": "Those are my books", "Published": True, "Rating": 4, "Id": 2},]
#region Functions

def find_post_by_id(id: int):
    for post in my_posts:
        if post["Id"] == id:
            return post
    return None
#endregion

#region Requests
@app.get("/")
def root():
    return {"message": "Hello World this is initial page for the FastAPI."}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM "tblPosts";""")
    posts = cursor.fetchall()
    return {"Data": posts}

@app.get("/posts/{id}")
def get_post_by_id(id: int, response: Response):
    cursor.execute("""SELECT * FROM "tblPosts" WHERE "Id" = %s;""", (str(id)))
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    return {"Data": post}

@app.post("/posts/create", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO "tblPosts" ("Title", "Content", "Published") VALUES (%s, %s, %s) RETURNING * ;""", (post.Title, post.Content, post.Published))
    new_post = cursor.fetchone()
    connection.commit()
    return {"Data": new_post}

@app.delete("/posts/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM "tblPosts" WHERE "Id" = %s RETURNING * ;""", (str(id),))
    deleted_post = cursor.fetchone()
    connection.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE "tblPosts" SET "Title" = %s, "Content" = %s, "Published" = %s WHERE "Id" = %s RETURNING * ;""", (post.Title, post.Content, post.Published, str(id)))
    updated_post = cursor.fetchone()
    connection.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} was not found")

    return {"Data": updated_post}
#endregion