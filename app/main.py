from fastapi import FastAPI
import firebase
app=FastAPI()

from database import db_connect

@app.on_event("startup")
async def startup():
    await db_connect()

@app.get('/')
def root():
    return {"message":"Qble Backend runnning from giri helloo guyzzz"}
