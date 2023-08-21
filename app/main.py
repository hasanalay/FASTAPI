from fastapi import Depends, FastAPI
import time
import psycopg2
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
from .database import engine, get_db
from . import models
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
#region Requests

@app.get("/")
def root():
    return {"message": "Hello World this is initial page for the FastAPI."}

# endregion