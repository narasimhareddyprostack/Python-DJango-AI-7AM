from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

users=[]

class User(BaseModel):
    uname:str 
    loc:str 
    email:str

'''
Usage:create new user
API URL:http://127.0.0.01:8000/create
API URL:http://127.0.0.01:8000/
Method Type:POST
Required Fields:uname,loc,email
Access Type:Public
'''
@app.post('/create')
def craete_user(user:User):
    print(user)
    users.append(user)
    return {"msg":"user created","user":user}

'''
Read
---------
Usage:featch all users
API URL:http://127.0.0.01:8000/read
API URL:http://127.0.0.01:8000/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/read")
def get_users():
    return users