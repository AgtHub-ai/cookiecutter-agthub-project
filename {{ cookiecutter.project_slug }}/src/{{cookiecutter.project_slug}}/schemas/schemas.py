from typing import List
from pydantic import BaseModel, Field



class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ItemListResponse(BaseModel):
    items: List[Item]
    next_cursor: int = 0

    @classmethod
    def from_data(cls, items: List[Item], next_cursor: int = 0):
        return cls(items=items, next_cursor=next_cursor)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class UserListResponse(BaseModel):
    users: List[User]
    next_cursor: int = 0

    @classmethod
    def from_data(cls, users: List[User], next_cursor: int = 0):
        return cls(users=users, next_cursor=next_cursor)