from sqlalchemy.orm import Session
from ..models.dao.user_dao import UserDao
from ..schemas.schemas import UserCreate
from ..schemas import schemas
from ..models import User


class UserService:
    db: Session
    user_dao: UserDao

    def __init__(self, db: Session):
        if (hasattr(self, 'db') is False) or self.db is None:
            self.db = db
            self.user_dao = UserDao.instance(db)
   
    def create_user(self, user: UserCreate): 
        new_user = User()
        new_user.email = user.email
        new_user.hashed_password= user.password+"$HASH"
        return self.user_dao.create(new_user)
    
    def get_user_by_email(self, email) -> User: 
        return self.user_dao.query().filter(
                User.email == email,
            ).one_or_none()
    
    def get_users(self, skip: int = 0,cursor: int=0, limit: int = 100):
        query_results, next_cursor = self.user_dao.list_objects(cursor, limit)
        return query_results, next_cursor
    
    def get(self, id: int = 0):
        return self.user_dao.get(id)