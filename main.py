import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv(".env")

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


