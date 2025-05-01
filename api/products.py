from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db import database
from schemas import products_schemas
from repository import products_rep

get_db = database.get_db


router = APIRouter(tags=['Продукти 🛍️'], prefix="/products")


@router.get("/", response_model=list[products_schemas.ShowAllProducts], status_code=status.HTTP_200_OK)
def get_all(db:Session = Depends(get_db)):
  return products_rep.get_all(db)

@router.get("/{id}/", response_model=products_schemas.ShowAllProducts, status_code=status.HTTP_200_OK)
def get_one(id:int, db:Session = Depends(get_db)):
  return products_rep.get_one(id, db)

