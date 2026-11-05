from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def root():
    return {"message":"Qble Backend runnning just now added CI V2 Hello World"}
