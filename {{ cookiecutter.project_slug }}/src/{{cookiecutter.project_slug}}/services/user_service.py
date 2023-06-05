from sqlalchemy.orm import Session
from ..models.repository.user_repo import UserRepository
from ..schemas.schemas import UserCreate
from ..schemas import schemas
from ..models import User


class UserService:
    db: Session
    user_repo: UserRepository

    def __init__(self, db: Session):
        if (hasattr(self, 'db') is False) or self.db is None:
            self.db = db
            self.user_repo = UserRepository.instance(db)
   
    def create_user(self, user: UserCreate): 
        new_user = User()
        new_user.email = user.email
        new_user.hashed_password= user.password+"$HASH"
        return self.user_repo.create(new_user)
    
    def get_user_by_email(self, email) -> User: 
        return self.user_repo.query().filter(
                User.email == email,
            ).one_or_none()
    
    def get_users(self, skip: int = 0,cursor: int=0, limit: int = 100):
        query_results, next_cursor = self.user_repo.list_objects(cursor, limit)
        return query_results, next_cursor
    
    def get(self, id: int = 0):
        return self.user_repo.get(id)