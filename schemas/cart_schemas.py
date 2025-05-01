from pydantic import BaseModel
from schemas import products_schemas
from typing import Optional

class AddToCart(BaseModel):
    product_id: int
    quantity: int

class ShowProductCartItem(BaseModel):
    name: str
    price: float
    quantity: int

    class Config:
        orm_mode = True

class ShowProductCart(BaseModel):
    items: list[ShowProductCartItem]
    
