from sqlalchemy.orm import Session
from .base_repo import BaseRepository
from .. import Item


class ItemRepository(BaseRepository):
    _instance = None

    @classmethod
    def instance(cls, session: Session):
        if cls._instance is None:
            cls._instance = cls(session)
        return cls._instance

    def __init__(self, session: Session):
        if ItemRepository._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super().__init__(session, Item)
            ItemRepository._instance = self