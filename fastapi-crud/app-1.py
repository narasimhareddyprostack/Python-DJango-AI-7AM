from fastapi import FastAPI
app=FastAPI()

'''
USAGE: Application Root Request
API URL:http://127.0.0.1:8000/
Method Type:GET
'''
@app.get("/")
def root_req():
    return {"msg":"Application Root Request"}

'''
Usage:create new user
API URL:http://127.0.0.01:8000/create
API URL:http://127.0.0.01:8000/
Method Type:POST
Required Fields:uname,loc,email
Access Type:Public
'''
@app.post('/create')
def craete_user():
    return {"msg":"user created"}

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
    return {"msg":'Fetching User Details'}

'''
Update
------------
Usage:update User by Id
API URL:http://127.0.0.01:8000/update/101
API URL:http://127.0.0.01:8000/101
Method Type:PUT
Required Fields:uname,uloc,uemail
Access Type:Public
'''
@app.put("/update/{uid}")
def update_user(uid:int):
    print(uid)
    return {"msg":"user updated successfully","uid":uid}


'''
Delete
------
Usage:delete User by id
API URL:http://127.0.0.01:8000/delete/101
API URL:http://127.0.0.01:8000/101
Method Type:DELETE
Required Fields:None
Access Type:Public
'''
@app.delete("/delete/{uid}")
def delete_user(uid:int):
    print(uid)
    return {"msg":"User Deleted successfully"}