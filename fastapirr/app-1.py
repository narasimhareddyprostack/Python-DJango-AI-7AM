from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def indexpage():
    return {'messsage':'Index Page'}

@app.get("/user")
def userpage():
    return {"message":"User Page"}