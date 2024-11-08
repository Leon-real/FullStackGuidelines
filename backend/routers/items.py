from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models

router = APIRouter()

@router.get("/items/", response_model=List[dict])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return [{"id": item.id, "name": item.name, "description": item.description} for item in items]

@router.post("/items/", response_model=dict)
def create_item(item: dict, db: Session = Depends(get_db)):
    db_item = models.Item(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id": db_item.id, "name": db_item.name, "description": db_item.description}