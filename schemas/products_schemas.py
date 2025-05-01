from pydantic import BaseModel


class ShowAllProducts(BaseModel):
  id:int
  name:str
  description:str
  price: float
    
  class Config():
      orm_mode = True
      
      
class ProductOut(BaseModel):
  id:int
  name:str
  price: float
