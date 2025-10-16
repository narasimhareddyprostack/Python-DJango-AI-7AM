from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 

app= FastAPI()

employees=[]

class Employee(BaseModel):
    ename:str 
    esal:float
    loc:str 
    age:int 

'''
Usage:Root Request
API URL:http://127.0.0.1:8000/
Method Type:GET
'''
@app.get("/")
def index_page():
    return {"message":"Index Page"}


'''
Usage:create new employee
API: http://127.0.0.1:8000/create
Method Type:POST
Required Fields:ename,esal,loc,age
Access Type:Public
'''

@app.post("/create")
def create_Employee(employee:Employee):
    employees.append(employee)
    return {"employee":employee,"message":"New Employee Created"}



'''
usage:fetch all employees
API URL:http//127.0.0.1:8000/read
Method Type:GET
Required Fields:None
'''
@app.get("/read")
def get_employees():
    return employees