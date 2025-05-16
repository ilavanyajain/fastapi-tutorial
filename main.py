from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def get_api():
    return "Hello World"