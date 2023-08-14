from typing import List
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"] 
)
# region User requests

@router.get("/", response_model=List[schemas.UserOutput])
def get_posts(db: Session = Depends(get_db)):
    users=db.query(models.User).all()
    return users

@router.get("/{id}", response_model=schemas.UserOutput)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.Id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id: {id} was not found")
    return user

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOutput)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash_password(user.Password)
    user.Password=hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# endregion