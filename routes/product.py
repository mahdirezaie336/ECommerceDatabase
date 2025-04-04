from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from models import Product as ProductModel
from schemas import Product as ProductSchema
from database import get_db

router = APIRouter()

@router.get("/discounted-products")
def get_discounted_products(
    store: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    min_discount: float = Query(0),
    db: Session = Depends(get_db)
) -> List[ProductSchema]:
    """
    Get a list of products with a discount greater than or equal to the specified minimum discount.
    """
    query = db.query(ProductModel).filter(ProductModel.discount_percent >= min_discount)

    if store:
        query = query.filter(ProductModel.store == store)
    if category:
        query = query.filter(ProductModel.category == category)

    products = query.all()
    return products
