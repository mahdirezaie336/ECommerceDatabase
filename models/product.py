from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    original_price = Column(String)
    discounted_price = Column(String)
    discount_percent = Column(Float)
    purchase_url = Column(String)
    image_url = Column(String)
    store = Column(String)
    category = Column(String)
