from fastapi import Depends, Response, status, HTTPException, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/like",
    tags=["Likes"]
)

@router.post("", status_code=status.HTTP_201_CREATED)
def like_post(like: schemas.Like, db:Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.Id == like.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    like_query = db.query(models.Like).filter(models.Like.UserId == current_user.Id, models.Like.PostId == like.post_id)
    found_like= like_query.first()
    
    if (like.dir == 1):
        if found_like:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You already liked this post")
        new_like = models.Like(UserId=current_user.Id, PostId=like.post_id)
        db.add(new_like)
        db.commit()
        return{"message": "Post liked"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You have not liked this post")
        like_query.delete(synchronize_session=False)
        db.commit()
        return{"message": "Post unliked"}