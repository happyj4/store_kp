from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, TIMESTAMP, DECIMAL, CheckConstraint, func, Double
from .database import Base
from sqlalchemy.orm import relationship


class Product(Base):
  __tablename__ = 'products'
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  description = Column(Text)
  price = Column(DECIMAL(10, 2), nullable=False)
  
  carts = relationship("Cart", back_populates="product", cascade="all, delete-orphan")
  
  
  
  
class Cart(Base):
  __tablename__ = 'carts'
  
  id = Column(Integer, primary_key=True, index=True)
  product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
  quantity = Column(Integer, nullable=False)
  
  product = relationship("Product", back_populates="carts")
  

  