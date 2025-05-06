from pydantic import BaseModel
from schemas import products_schemas
from typing import Optional
from schemas import products_schemas

ShowAllProducts = products_schemas.ShowAllProducts
from pydantic import BaseModel

class AddToCart(BaseModel):
    product_id: int
    quantity: int = 1

class ShowProductCartItem(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

    class Config:
        orm_mode = True

class ShowProductCart(BaseModel):
    items: list[ShowProductCartItem]

