from fastapi import FastAPI
from .database import engine
from . import models
from .routers import post, user, auth, like
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(like.router)
#region Requests

@app.get("/")
def root():
    return {"message": "Hello World this is initial page for the FastAPI."}

# endregion