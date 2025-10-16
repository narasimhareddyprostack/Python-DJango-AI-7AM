from fastapi import FastAPI

app=FastAPI()

#create - http://127.0.0.1:8000/login
@app.post("/login")
def login_page():
    return {'message':'login page'}


#read - http://127.0.0.1:8000/users
@app.get("/users")
def get_userdetails():
    return {'message':'user details'}

#update - http://127.0.0.1:8000/user
@app.put("/user")
def update_user():
    return {'message':'update user'}

#delete  - http://127.0.0.1:8000/user
@app.delete("/user")
def delete_user():
    return {"message":"delete user"}