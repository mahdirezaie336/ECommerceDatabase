from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from models.product import Product
from database import get_db

router = APIRouter()


@router.get("/discounted-products", response_model=List[Product])
def get_discounted_products(
        store: str = Query(None),
        category: str = Query(None),
        min_discount: float = Query(0),
        db: Session = Depends(get_db)
):
    query = db.query(Product).filter(Product.discount_percent >= min_discount)

    if store:
        query = query.filter(Product.store == store)
    if category:
        query = query.filter(Product.category == category)

    products = query.all()
    return products
