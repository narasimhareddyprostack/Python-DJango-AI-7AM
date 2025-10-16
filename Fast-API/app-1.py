from fastapi import FastAPI

#create FastAPI app
app=FastAPI()

print(type(app))

#develop API
'''
API Usage: Application Root request
URL:http://127.0.0.1:8000/
Method Type:GET
required Fields: None
Access Type:Public
'''
@app.get("/")
def indexpage():
    return {"message":"Index Page"} 


'''
API Usage: Application About Page request
URL:http://127.0.0.1:8000/about
Method Type:GET
required Fields: None
Access Type:Public
'''
@app.get("/about")
def aboutpage():
    return {"message":"About Page"}
