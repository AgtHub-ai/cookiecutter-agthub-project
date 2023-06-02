from fastapi import Depends, APIRouter, HTTPException
from ..schemas import schemas
from ..models.dao import user_dao
from ..models import User
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import UserService

router = APIRouter(tags=["Users"])

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(user=user)


@router.get("/users/", response_model=schemas.UserListResponse)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_service = UserService(db)
    users, cursor = user_service.get_users(skip=skip, limit=limit)
    return schemas.UserListResponse(users=users, next_cursor=cursor)


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.User.from_orm(db_user)
