from sqlalchemy.orm import Session
from .base_dao import BaseDao
from .. import Item


class ItemDao(BaseDao):
    _instance = None

    @classmethod
    def instance(cls, session: Session):
        if cls._instance is None:
            cls._instance = cls(session)
        return cls._instance

    def __init__(self, session: Session):
        if ItemDao._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super().__init__(session, Item)
            ItemDao._instance = self