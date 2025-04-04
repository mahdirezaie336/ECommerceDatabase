from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    original_price: str
    discounted_price: str
    discount_percent: float
    purchase_url: str
    image_url: str
    store: str
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    # class Config:
    #     orm_mode = True
