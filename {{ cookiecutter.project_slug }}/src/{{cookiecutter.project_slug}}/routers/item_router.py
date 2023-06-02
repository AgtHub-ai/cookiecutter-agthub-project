from fastapi import Depends, APIRouter, HTTPException
from ..services import ItemService
from ..schemas import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from loguru import logger

router = APIRouter(tags=["Items"])

@router.get("/items/", response_model=schemas.ItemListResponse)
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = ItemService(db)
    items, next_cur = service.read_items(limit=limit)
    logger.info("That's it, beautiful and simple logging!")
    return schemas.ItemListResponse(items=items, next_cursor=next_cur)

@router.get("/items/{item_id}")
def get_by_id(skip: int = 0, item_id: int = 0, db: Session = Depends(get_db)):
    service = ItemService(db)
    item = service.get_item(item_id)
    return schemas.Item.from_orm(item)