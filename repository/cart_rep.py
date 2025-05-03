from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db import models
from schemas import cart_schemas, products_schemas


AddToCart = cart_schemas.AddToCart
ShowProductCart = cart_schemas.ShowProductCart
ShowProductCartItem = cart_schemas.ShowProductCartItem


def add_to_cart(request: AddToCart, db: Session):

    product = db.query(models.Product).filter(models.Product.id == request.product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не знайдено")


    cart_item = db.query(models.Cart).filter(models.Cart.product_id == request.product_id).first()
    if cart_item:
        cart_item.quantity += request.quantity
    else:
        cart_item = models.Cart(product_id=request.product_id, quantity=request.quantity)
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)
    return {"message": "Продукт додано до кошика"}


def show(db: Session) -> ShowProductCart:
    cart_items = db.query(models.Cart).all()
    result = []

    for item in cart_items:
        result.append(ShowProductCartItem(

            name=item.product.name,
            price=float(item.product.price),
            quantity=item.quantity
        ))

    return ShowProductCart(items=result)


def destroy(id, db:Session):
    cart_item = db.query(models.Cart).filter(models.Cart.product_id == id).delete(synchronize_session=False)
    db.commit()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Товар з id = {id} не знайдено")
    return 
    
