from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator,ValidationError

#create FastAPI app 
app=FastAPI()
#create root requrest
#URL:http://127.0.0.1:8000/
@app.get("/")
def home_page():
    return {"msg":"Application Home Page"}


class Product(BaseModel):
    pname:str = Field(...)
    price:float=Field(..., gt=1000)
    qty:int  =Field(...,ge=1)
    info:str =Field(...)

   
    @field_validator('qty')
    @classmethod
    def check_qty(cls,qty:int)->int:
        if qty > 100:
            raise ValueError("Product Qty - allowed max value 100")
        return qty
    

'''
Usage: create new product
API URL:http://127.0.0.1:8000/api/
Method Type:POST
Required Fields:pname,price,qty,info
Access Type:public
'''
@app.post("/api")
async def create_product(product:Product):
    print(product)
    return {"product_data":product}