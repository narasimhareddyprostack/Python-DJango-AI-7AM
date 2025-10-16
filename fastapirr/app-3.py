from fastapi import FastAPI,HTTPException

app=FastAPI()

#user table data 
users={
    101:{'uname':'Rahul Gandhi'},
    102:{'uname':'Sonai Gandhi'},
    103:{'uname':'Priyanka Gandhi'},
    104:{'uname':'Modi'},
}

#API URL:http://127.0.0.1:8000/
@app.get("/")
def index_page():
    return {'message':'Index Page'}



'''
USAGE:Fetch user by Id
API URL:http://127.0.0.1:8000/user/101
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/user/{user_id}")
def user_details(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404,detail='user not found')
    return users[user_id]
        
    


'''
USAGE : fetch all users
API URL:http://127.0.0.1:8000/users/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/users")
def fetch_allusers():
    return users