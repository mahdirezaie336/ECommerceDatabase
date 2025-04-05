from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    original_price = Column(Float)
    discounted_price = Column(Float)
    discount_percent = Column(Float)
    purchase_url = Column(String)
    image_url = Column(String)
    store = Column(String)
    category = Column(String)

    def __repr__(self):
        return (f"<Product(name={self.name}, original_price={self.original_price}, "
                f"category={self.category})>")
