from fastapi import FastAPI
from api import products, cart

app = FastAPI()


app.include_router(products.router)
app.include_router(cart.router)
