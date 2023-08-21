from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=["Authentication"])

@router.post('/login', response_model=schemas.Token)
def login (user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.Email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials!")
    # veriyf users password
    if not utils.verify(user_credentials.password, user.Password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials!")
    
    access_token = oauth2.create_access_token(data={"user_id": user.Id})
    
    return {"Access_token": access_token, "Token_type": "bearer"}
    