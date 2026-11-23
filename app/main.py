from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def root():
    return {"message":"Qble Backend runnning from giri helloo guyzzz"}
