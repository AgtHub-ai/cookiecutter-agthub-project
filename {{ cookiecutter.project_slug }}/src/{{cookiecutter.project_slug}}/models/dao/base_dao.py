from abc import ABC
from sqlalchemy.orm import Session
import sys

class BaseDao(ABC):

    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def get(self, item_id: int):
        return self.session.query(self.model).filter(self.model.id == item_id).first()

    def get_by_ids(self, ids: list):
        return self.session.query(self.model).filter(self.model.id.in_(ids)).all()

    def create(self, item):
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def update(self, item_id: int, updated_item: dict):
        item = self.session.query(self.model).filter(self.model.id == item_id).first()
        if item:
            for key, value in updated_item.items():
                setattr(item, key, value)
            self.session.commit()
            self.session.refresh(item)
        return item

    def delete(self, item_id: int) -> bool:
        item = self.session.query(self.model).filter(self.model.id == item_id).first()
        if item:
            self.session.delete(item)
            self.session.commit()
            return True
        return False

    def list_objects_with_filter(self, criterion, cursor: int = 0, limit: int = 10):
        cursor = cursor if cursor > 0 else sys.maxsize
        query_results = self.session.query(self.model).filter(
            criterion, self.model.id <= cursor).order_by(self.model.id.desc()).limit(limit).all()

        if query_results is None:
            return None, 0

        next_cursor = 0
        if len(query_results) >= limit:
            next_cursor = query_results[-1].id - 1

        return query_results, next_cursor

    def list_objects(self, cursor: int = 0, limit: int = 10):
        cursor = cursor if cursor > 0 else sys.maxsize
        query_results = self.session.query(self.model).filter(self.model.id <= cursor).order_by(
            self.model.id.desc()
        ).limit(limit).all()

        if query_results is None:
            return None, 0

        next_cursor = 0
        if len(query_results) >= limit:
            next_cursor = query_results[-1].id - 1

        return query_results, next_cursor

    def query(self):
        return self.session.query(self.model)
