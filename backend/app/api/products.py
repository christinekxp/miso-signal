from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.models import Product
from app.schema.product import ProductResponse

router = APIRouter()

@router.get("/products", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()