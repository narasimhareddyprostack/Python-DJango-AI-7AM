from fastapi import FastAPI

#create fastapi app

app=FastAPI()
'''
API URL: http://localhost:8000/
Method Type:GET
'''
@app.get("/")
def indexpage():
    return {"message":"Index Page"} 

'''
API URL: http://localhost:8000/about
Method Type:GET
'''
@app.get("/about")
def aboutpage():
    return {"message":"About Page"} 


'''
API URL: http://localhost:8000/contact
Method Type:GET
'''
@app.get("/contact")
def contactpage():
    return {"message":"Contact Page"}

'''
API URL: http://localhost:8000/login
Method Type:POST
'''
@app.post("/login")
def loginpage():
    return {"message":"Login"}