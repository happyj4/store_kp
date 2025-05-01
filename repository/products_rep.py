from fastapi import HTTPException,  status
from sqlalchemy.orm import Session
from db import models


def get_all(db: Session):
  products = db.query(models.Product).all()
  return products

def get_one(id,db: Session):
  product = db.query(models.Product).filter(models.Product.id == id).first()
  if not product:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Продукт за id = {id} не знайдено")
  return product