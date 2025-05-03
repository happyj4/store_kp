from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session
from db import database
from schemas import products_schemas, cart_schemas
from repository import cart_rep
from typing import Annotated

get_db = database.get_db


router = APIRouter(tags=['Кошик 🛒'], prefix="/cart")


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_to_cart(request: cart_schemas.AddToCart, db: Session = Depends(get_db)):
    return cart_rep.add_to_cart(request, db)


@router.get("/", response_model=cart_schemas.ShowProductCart, status_code=status.HTTP_200_OK)
def show_cart(db: Session = Depends(get_db)):
    return cart_rep.show(db)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:Annotated[int, Path(ge=1, lt=100)] ,db: Session = Depends(get_db)):
    return cart_rep.destroy(id, db)