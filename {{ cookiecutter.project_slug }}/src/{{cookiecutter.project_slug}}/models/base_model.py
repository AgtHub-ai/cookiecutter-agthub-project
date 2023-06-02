class BaseModel:
    def to_dict(self):
        return {c.title: getattr(self, c.title, None) for c in self.__table__.columns}
