from ..models.dao.item_dao import ItemDao
from sqlalchemy.orm import Session
from ..schemas.schemas import UserCreate
from ..models import User


class ItemService:
    db: Session
    item_dao: ItemDao

    def __init__(self, db: Session):
        if (hasattr(self, 'db') is False) or self.db is None:
            self.db = db
            self.item_dao = ItemDao.instance(db)
   
    def read_items(self, limit: int = 10): 
        return self.item_dao.list_objects(limit=limit)
    
    def get_item(self, id: int = 0): 
        return self.item_dao.get(id)